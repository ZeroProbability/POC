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
    con = cx_Oracle.connect('{0}/{1}@main.pc:1521/orcl'.format(user, password))

def create_schema(schema_name):
    cur=admcon.cursor()
    try:
        cur.execute("CREATE USER {0} IDENTIFIED BY {0}".format(schema_name))
        print "created user {0}".format(schema_name)
    except Exception, e:
        if str(e.message).startswith("ORA-01920:"):  # user already exists
            reset_user_connection(schema_name, schema_name)
            cur.close()
            return
    cur.execute("GRANT CONNECT TO {0}".format(schema_name))
    cur.execute("GRANT CREATE SESSION TO {0}".format(schema_name))
    cur.execute("GRANT CREATE TABLE TO {0}".format(schema_name))
    cur.execute("GRANT CREATE VIEW TO {0}".format(schema_name))
    reset_user_connection(schema_name, schema_name)
    cur.close()

def create_tables(schema_name):
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

def create_objects(dirname, object_type, schema_name):
    print "{0}/{1}".format(schema_name, dirname)
    if not os.path.isdir("{0}/{1}".format(schema_name, dirname)):
        return
    cur=con.cursor()
    for file in os.listdir("{0}/{1}".format(schema_name, dirname)):
        f=open("{0}/{1}/{2}".format(schema_name, dirname, file), "r")
        sql_lines=f.readlines()
        f.close()
        sql="".join(sql_lines)
        sql_without_semicolon=re.findall('(.*?);',sql, re.DOTALL)
        print sql_without_semicolon
        cur.execute(sql_without_semicolon[0]);

def main(argv):
    global admcon
    admcon = cx_Oracle.connect('sys/oracle@main.pc:1521/orcl', mode=cx_Oracle.SYSDBA)

    for schema in ('FEDM', 'FEODS', 'FEAUDIT'):
        create_schema(schema)
        create_tables(schema)
    for schema in ('FEDM', 'FEODS', 'FEAUDIT'):
        reset_user_connection(schema, schema)
        create_objects('VIEW', 'view', schema)

if __name__ == '__main__':
    main(sys.argv[1:])
