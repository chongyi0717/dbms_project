from pickle import FALSE
import mysql.connector

class sql_connecter:
    def __init__(self):
        self.connection=mysql.connector.connect(user="root",password="0000")
        self.cursor=self.connection.cursor()
        self.database=""
    def create_database(self,name):
        self.cursor.execute("show databases;")
        records=self.cursor.fetchall()
        a=False
        for r in records:
            if name in r:
                a=True
        if(a==False):
            self.cursor.execute("create database "+name+";")
        self.database=name
        
    def show_database(self):
        self.cursor.execute("show databases;")
        records=self.cursor.fetchall()
        a=False
        for r in records:
            print(r)
    def drop_database(self):
        self.cursor.execute("show databases;")
        records=self.cursor.fetchall()
        a=False
        for r in records:
            if self.database in r:
                a=True
        if(a==True):
            self.cursor.execute("drop database "+self.database+";")
    def use_database(self):
        self.cursor.execute("show databases;")
        records=self.cursor.fetchall()
        a=False
        for r in records:
            if self.database in r:
                a=True
        if(a==True):
            self.cursor.execute("use "+self.database+";")
    def create_table(self,name,parameters):
        self.cursor.execute("show tables;")
        records=self.cursor.fetchall()
        a=False
        for r in records:
            if name in r:
                a=True
        if(a==False):
            self.cursor.execute("create table "+name+"("+parameters+");")
        self.table=name
    def show_tables(self):
        self.cursor.execute("show tables;")
        records=self.cursor.fetchall()
        a=False
        for r in records:
            print(r)
    def describe_table(self):
        self.cursor.execute("describe "+self.table+";")
        records=self.cursor.fetchall()
        a=False
        for r in records:
            print(r)
    
    def drop_table(self,name):
        self.cursor.execute("show tables;")
        records=self.cursor.fetchall()
        a=False
        for r in records:
            if name in r:
                a=True
        if(a==True):
            self.cursor.execute("drop table "+name+";")
    def insert_table(self,name,parameters):
        self.cursor.execute("show tables;")
        records=self.cursor.fetchall()
        a=False
        for r in records:
            if name in r:
                a=True
        if(a==True):
            self.cursor.execute("insert into "+name+" values("+parameters+");")
    
    def show(self,instruction):
        self.cursor.execute(instruction)
        records=self.cursor.fetchall()
        fields=self.cursor.description
        field_list=[]
        for i in fields:
            field_list.append(i[0])
        list=[[]]
        for r in records:
            list1=[]
            for i in r:                
                list1.append(i)
            list.append(list1)
        return list,field_list
    def input_commend(self,commend):
        self.cursor.execute(commend+";")
    def close(self):
        self.cursor.close()
        self.connection.commit()
        self.connection.close()

# sql=sql_connecter()
# sql.create_database("sql_tutorial")
# sql.use_database()
# sql.create_table("student","student_id int,name varchar(20)")
# sql.drop_table("student")
# sql.drop_table("teacher")
# sql.drop_table("class")
# sql.drop_table("book")
# sql.drop_table("teach")
# sql.close()
