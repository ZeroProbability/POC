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

def create_schema(schema_name):
    print "CREATE USER {0} IDENTIFIED BY {0};".format(schema_name)
    print "GRANT CONNECT TO {0};".format(schema_name)
    print "GRANT CREATE SESSION TO {0};".format(schema_name)
    print "GRANT CREATE TABLE TO {0};".format(schema_name)

def create_tables(schema_name):
    for file in os.listdir(schema_name+"/TABLE"):
        print (20*"=")+file+(20*"=")
        sqls=get_create_table_sql_from_file(schema_name+"/TABLE/"+file)
        cur=con.cursor()
        try:
            cur.execute("drop table {0}.{1}".format(schema_name, str(file).replace(".sql","")))
        except Exception, e:
            if not str(e.message).startswith("ORA-00942:"):
                raise e
        for sql in sqls:
            print "->"+str(sql)
            try:
                cur.execute(sql);
            except Exception, e:
                if not str(e.message).startswith("ORA-00955:"):
                    raise e

def create_views(schema_name):
    for file in os.listdir(schema_name+"/VIEW"):
        print (20*"=")+file+(20*"=")
        print file

def main(argv):
    global con
    con = cx_Oracle.connect('FEDM/FEDM@main.pc:1521/orcl')

    create_schema('FEDM')
    create_tables('FEDM')
    create_views('FEDM')

if __name__ == '__main__':
    main(sys.argv[1:])
