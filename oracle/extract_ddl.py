#!/usr/bin/env python
# encoding: utf-8

import cx_Oracle
import os
import sys, getopt

def generic_ddl(owner, object_type, object_name):
    # read the views
    cur = con.cursor()
    print "%s %s %s"%(owner, object_type, object_name)
    cur.execute("SELECT DBMS_METADATA.GET_DDL(replace(object_type, ' ', '_'), object_name, owner) FROM DBA_OBJECTS WHERE (owner = '{0}' and object_type='{1}' and object_name='{2}')".format(owner, object_type, object_name))

    row=cur.fetchone()
    obj_ddl_str=row[0].read()
    obj_ddl_str=obj_ddl_str.rstrip()
    if(obj_ddl_str[-1] != ';'):
        obj_ddl_str+=';'
    return obj_ddl_str

def ddl_extract_of_generic_type(owner, object_type):
    # read the views
    cur = con.cursor()
    cur.execute("SELECT object_name FROM DBA_OBJECTS WHERE (owner = '{0}' and object_type='{1}')".format(owner, object_type))
    
    file_path="{0}/{1}".format(owner, object_type)

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    for obj_name, in cur:
        ddl_file = open( "{0}/{1}.sql".format(file_path, obj_name), "w")
        ddl_file.write("-"*80+"\n")
        ddl_file.write("-- DDL for {0} : {1}.{2}\n".format(object_type, owner, obj_name))
        ddl_file.write("-"*80+"\n")
        ddl_file.write(generic_ddl(owner, object_type, obj_name))
        ddl_file.close()

def ddl_extract_of_table(owner):
    # read the views
    cur = con.cursor()
    object_type='TABLE'
    cur.execute("""
    begin
        dbms_metadata.set_transform_param( dbms_metadata.session_transform,
            'SQLTERMINATOR', TRUE);
        dbms_metadata.set_transform_param( dbms_metadata.session_transform,
            'STORAGE', FALSE);
        dbms_metadata.set_transform_param( dbms_metadata.session_transform,
            'TABLESPACE', FALSE);
        dbms_metadata.set_transform_param( dbms_metadata.session_transform,
            'SEGMENT_ATTRIBUTES', FALSE);
        dbms_metadata.set_transform_param( dbms_metadata.session_transform,
            'CONSTRAINTS_AS_ALTER', TRUE);
        dbms_metadata.set_transform_param( dbms_metadata.session_transform,
            'PARTITIONING', FALSE);
    end;""")

    cur.execute("SELECT object_name FROM DBA_OBJECTS WHERE (owner = '{0}' and object_type='{1}')".format(owner, object_type))

    file_path="{0}/{1}".format(owner, object_type)

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    for table_name, in cur:
        ddl_file = open( "{0}/{1}.sql".format(file_path, table_name), "w")
        ddl_file.write("-"*80+"\n")
        ddl_file.write("-- DDL for {0} : {1}.{2}\n".format(object_type, owner, table_name))
        ddl_file.write("-"*80+"\n")
        ddl_file.write(generic_ddl(owner, object_type, table_name)+"\n")

        col_comments_cur=con.cursor()
        col_comments_cur.execute("SELECT column_name, comments FROM all_col_comments WHERE owner='{0}' AND table_name='{1}' and comments is not null".format(owner, table_name))

        comments_str=""
        for column_name, col_comment, in col_comments_cur:
            comments_str+='  COMMENT ON COLUMN "{0}"."{1}"."{2}" IS \'{3}\';\n'.format(owner, table_name, column_name, col_comment.replace("'", "''"))
        if col_comments_cur.rowcount > 0:
            ddl_file.write("\n"+comments_str)

        index_cur=con.cursor()
        index_cur.execute("SELECT index_name FROM all_indexes WHERE owner = '{0}' AND table_name='{1}'".format(owner, table_name))

        for index_name, in index_cur:
            ddl_file.write("\n")
            ddl_file.write("-"*80+"\n")
            ddl_file.write("-- DDL for {0} : {1}.{2}\n".format('INDEX', owner, index_name))
            ddl_file.write("-"*80+"\n")
            ddl_file.write(generic_ddl(owner, 'INDEX', index_name)+"\n")

        constraint_cur=con.cursor()
        sql="""
        SELECT constraint_type, 
               dbms_metadata.get_ddl('CONSTRAINT',constraint_name,owner) 
           FROM all_constraints 
           WHERE owner='%s' AND table_name='%s' AND constraint_type<>'R'
        """
        constraint_cur.execute(sql%(owner, table_name))

        constraints_full_str=""
        for constraint_type, constraint_str, in constraint_cur:
            constraints_full_str+=constraint_str.read()+"\n"
        if constraints_full_str != "":
            constraints_full_str="\n"+("-"*80)+"\n-- Constraints\n"+("-"*80)+"\n"+constraints_full_str
        ddl_file.write(constraints_full_str)


        ref_constraint_cur=con.cursor()
        sql="""
        SELECT constraint_type, 
               dbms_metadata.get_ddl('REF_CONSTRAINT',constraint_name,owner) 
           FROM all_constraints 
           WHERE owner='%s' AND table_name='%s' AND constraint_type='R'
        """
        ref_constraint_cur.execute(sql%(owner, table_name))
        
        constraints_full_str=""
        for constraint_type, constraint_str, in ref_constraint_cur:
            constraints_full_str+=constraint_str.read()+"\n"
        if constraints_full_str != "":
            constraints_full_str="\n"+("-"*80)+"\n-- Ref Constraints\n"+("-"*80)+"\n"+constraints_full_str
            ddl_file.write(constraints_full_str)

        ddl_file.close()

def main(argv):
    connect_string=''
    try:
        opts, args=getopt.getopt(argv,"hc:",["connectstring="])
    except getopt.GetoptError:
        print 'extract_ddl.py -c <connect_string>'
        print 'example: extract_ddl.py -c FEDM/FEDM@localhost:1521/orcl'
        sys.exit(1)
    for opt, arg in opts:
        if opt == '-h':
            print 'extract_ddl.py -c <connect_string>'
            print 'example: extract_ddl.py -c FEDM/FEDM@localhost:1521/orcl'
            sys.exit()
        elif opt in ("-c", "--connectstring"):
            connect_string = arg

    print "Connect String:%s\n"%(connect_string)

    global con
    con = cx_Oracle.connect(connect_string)

    for owner in ('FEDM','FEODS','FEAUDIT'):
        ddl_extract_of_table(owner)
        for otype in ('VIEW', 'PROCEDURE', 'PACKAGE', 'SEQUENCE', 'SYNONYM',
                'TRIGGER', 'MATERIALIZED VIEW', 'LIBRARY', 'TYPE', 'FUNCTION'):
            ddl_extract_of_generic_type(owner, otype)

    con.close()

if __name__ == '__main__':
    main(sys.argv[1:])
