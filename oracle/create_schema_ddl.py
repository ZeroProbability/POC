#!/usr/bin/env python
# encoding: utf-8

import cx_Oracle
import os
import sys, getopt
import re

def get_create_table_sql_from_file(file_name):
    return_sqls=[]
    f=open(file_name, "r")
    sql_lines=f.readlines()
    f.close()
    sql="".join(sql_lines)

    #-- create table statement 
    create_table_sql=re.search('(CREATE TABLE "[^"]+"\."[^"]+".*?\(.*?[^,][ \n]+\))',sql, re.DOTALL)
    if create_table_sql==None:
        create_table_sql=re.search('(CREATE GLOBAL TEMPORARY TABLE '
                +'"[^"]+"\."[^"]+".*?\(.*?[^,][ \n]+\))',sql, re.DOTALL)

    return_sqls.append(create_table_sql.group(0))

    #-- create index statement(s)
    create_index_sqls=re.findall('(CREATE INDEX "[^"]+"\."[^"]+" ON "[^"]+"\."[^"]+".*?\(.*?);',sql, re.DOTALL)
    return_sqls.extend(create_index_sqls)
    create_index_sqls=re.findall('(CREATE UNIQUE INDEX "[^"]+"\."[^"]+" ON "[^"]+"\."[^"]+".*?\(.*?);',sql, re.DOTALL)
    return_sqls.extend(create_index_sqls)

    #-- comment on column statement(s)
    comment_sqls=re.findall('(COMMENT ON COLUMN "[^"]+"\."[^"]+"\."[^"]+" IS \'.*?\');',sql, re.DOTALL)
    return_sqls.extend(comment_sqls)

    return return_sqls

def reset_user_connection(user, password):
    global con
    try:
        con.close()
    except Exception, e:
        pass # ignore 
    con = cx_Oracle.connect('{0}/{1}@main.pc:1521/orcl'.format(user, password))

def create_schema(schema_name, create_tablespace=True):
    cur=admcon.cursor()
    cur.execute("SELECT username FROM dba_users WHERE username='{0}'".format(schema_name))
    resultset=cur.fetchall()
    if len(resultset)>0:
        print "User {0} already exists. Dropping user..".format(schema_name)
        #TODO: make dropping optional
        cur.execute("DROP USER {0} CASCADE".format(schema_name))
    ts_part=""
    if create_tablespace:
        try:
            cur.execute("DROP TABLESPACE {0}_TS_DATA INCLUDING CONTENTS AND DATAFILES CASCADE CONSTRAINTS".format(schema_name))
        except Exception, e:
            pass   # TODO: check for errors
        cur.execute("CREATE TABLESPACE {0}_TS_DATA DATAFILE '/tfedata/{0}_TS_DATA' SIZE 10M AUTOEXTEND ON BLOCKSIZE 8K NOLOGGING ONLINE".format(schema_name))
        ts_part="DEFAULT TABLESPACE \"{0}_TS_DATA\"".format(schema_name)
    cur.execute("CREATE USER {0} IDENTIFIED BY {0} {1}"
            .format(schema_name, ts_part)
    )
    cur.execute("GRANT CONNECT TO {0}".format(schema_name))
    for object_type in ('SESSION', 'TABLE', 'VIEW', 'TYPE', 'MATERIALIZED VIEW',
            'SYNONYM', 'SEQUENCE', 'PROCEDURE'):
        cur.execute("GRANT CREATE {0} TO {1}".format(object_type, schema_name))
    reset_user_connection(schema_name, schema_name)
    cur.close()

def create_tables(schema_name):
    reset_user_connection(schema_name, schema_name)
    if not os.path.isdir(schema_name+"/TABLE"):
        return
    for file in os.listdir(schema_name+"/TABLE"):
        sqls=get_create_table_sql_from_file(schema_name+"/TABLE/"+file)
        cur=con.cursor()
        try:
            cur.execute("drop table {0}.{1}".format(schema_name, str(file).replace(".sql","")))
        except Exception, e:
            if not str(e.message).startswith("ORA-00942:"):   # does not exist
                raise e
        for sql in sqls:
            try:
                cur.execute(sql);
            except Exception, e:
                if not str(e.message).startswith("ORA-00955:"):   # object already exists
                    print "Error executing sql:\n"+sql
                    raise e

def create_objects(dirname, object_type, schema_name, terminal_char):
    reset_user_connection(schema_name, schema_name)
    cur=con.cursor()
    print "Reading sqls from {0}/{1}".format(schema_name, dirname)
    if not os.path.isdir("{0}/{1}".format(schema_name, dirname)):
        return
    for file in os.listdir("{0}/{1}".format(schema_name, dirname)):
        file_name="{0}/{1}/{2}".format(schema_name, dirname, file)
        f=open(file_name, "r")
        sql_lines=f.readlines()
        f.close()
        sql="".join(sql_lines)
        sql=re.sub('{0}[ \t\n]*$'.format(terminal_char),'',sql)
        try:
            cur.execute(sql);
        except Exception, e:
            print "error executing {0}".format(file_name)
            print sql
            raise e

def grant_table_access(from_user, to_user, access_type):
    cur=admcon.cursor()
    cur.execute("""SELECT object_name FROM DBA_OBJECTS WHERE (owner = '{0}' and object_type='{1}')
                      AND (owner, object_name) NOT IN (
                           SELECT owner, mview_name
                             FROM dba_mviews
                           UNION ALL
                           SELECT log_owner, log_table
                             FROM all_mview_logs
                      )
                """.format(from_user, 'TABLE'))
    tables=cur.fetchall()
    for table in tables:
        sql='GRANT {0} ON {1}.{2} TO {3}'.format(','.join(access_type), from_user, table[0], to_user)
        print sql
        cur.execute(sql)

def grant_select_access(from_user, to_user, object_type):
    cur=admcon.cursor()
    cur.execute("""SELECT object_name FROM DBA_OBJECTS WHERE (owner = '{0}' and object_type='{1}')
                """.format(from_user, object_type))
    objects=cur.fetchall()
    for obj in objects:
        sql='GRANT SELECT ON {0}.{1} TO {2}'.format(from_user, obj[0], to_user)
        cur.execute(sql)

def grant_execute_access(from_user, to_user, object_types):
    for object_type in object_types:
        cur=admcon.cursor()
        cur.execute("""SELECT object_name FROM DBA_OBJECTS WHERE (owner = '{0}' and object_type='{1}')
                    """.format(from_user, object_type))
        objects=cur.fetchall()
        for obj in objects:
            sql='GRANT EXECUTE ON {0}.{1} TO {2}'.format(from_user, obj[0], to_user)
            print sql
            try:
                cur.execute(sql)
            except Exception, e:
                pass  # TODO: handle

def main(argv):
    global admcon
    admcon = cx_Oracle.connect('sys/oracle@main.pc:1521/orcl', mode=cx_Oracle.SYSDBA)

#    for schema in ('FEDM', 'FEODS', 'FEAUDIT'):
#        create_schema(schema)
    create_schema('FEAPPBATCHUSER', create_tablespace=False)
#    for schema in ('FEDM', 'FEODS', 'FEAUDIT'):
#        create_tables(schema)
#    for object_type in ('VIEW', 'MATERIALIZED VIEW', 'TYPE', 'TRIGGER', 'SYNONYM', 'SEQUENCE'):
#        for schema in ('FEDM', 'FEODS', 'FEAUDIT'):
#            create_objects(object_type, object_type, schema, ';')
#    for object_type in ('FUNCTION', 'PROCEDURE', 'LIBRARY', 'PACKAGE'):
#        for schema in ('FEDM', 'FEODS', 'FEAUDIT'):
#            create_objects(object_type, object_type, schema, '/')
    for from_user in ('FEODS', 'FEAUDIT'):
        grant_table_access(from_user, 'FEDM', ('DELETE', 'INSERT', 'SELECT', 'UPDATE'))
        grant_table_access(from_user, 'FEAPPBATCHUSER', ('DELETE', 'INSERT', 'SELECT', 'UPDATE'))
        grant_select_access(from_user, 'FEDM', 'VIEW')
        grant_select_access(from_user, 'FEDM', 'SEQUENCE')
    for from_user in ('FEODS', 'FEDM'):
        grant_table_access(from_user, 'FEAPPBATCHUSER', ('DELETE', 'INSERT', 'SELECT', 'UPDATE'))
        grant_table_access(from_user, 'FEAUDIT', ('SELECT',))
        grant_select_access(from_user, 'FEAUDIT', 'VIEW')
        grant_select_access(from_user, 'FEAUDIT', 'SEQUENCE')
    for from_user in ('FEAUDIT', 'FEDM'):
        grant_table_access(from_user, 'FEAPPBATCHUSER', ('DELETE', 'INSERT', 'SELECT', 'UPDATE'))
        grant_table_access(from_user, 'FEODS', ('SELECT', 'INSERT'))
        grant_select_access(from_user, 'FEODS', 'VIEW')
        grant_select_access(from_user, 'FEODS', 'SEQUENCE')
    for from_user in ('FEAUDIT', 'FEODS'):
        grant_execute_access(from_user, 'FEDM', ('PACKAGE', 'PROCEDURE', 'FUNCTION'))
    for from_user in ('FEDM', 'FEAUDIT'):
        grant_execute_access(from_user, 'FEODS', ('PACKAGE', 'PROCEDURE', 'FUNCTION'))

if __name__ == '__main__':
    main(sys.argv[1:])
