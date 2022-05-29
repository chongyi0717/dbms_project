from cProfile import label
import encodings
from tkinter import *
from tkinter.ttk import *
from turtle import st
from functools import partial
from soupsieve import select
import pandas as pd
import csv
class My_Tk():
    def __init__(self,sql):
        self.tk=Tk()
        self.tk.geometry('620x600+500+100')
        self.orm={}
        self.sql=sql
        self.create()
        self.columns = ['日期', '楼房', '房号', '房租', '发送详情']
        self.widths = [100, 100, 100, 100, 100]
        #self.create_heading()
        self.create_tv()
        mainloop()
    def create(self):
        Label(self.tk, text="指令").pack()
        
        self.combo=Combobox(self.tk, 
                values=[
                        "SELECT-FROM-WHERE" , "DELETE" , "INSERT" , "UPDATE",
                        "IN", "NOT IN", "EXISTS", "NOT EXISTS",
                        "COUNT", "SUM", "MAX", "MIN", "AVG" , "HAVING",
                        "MYSQL"
                        ])
        self.combo.pack()
        Button(self.tk,text='確定',command=self.comfirm).pack()
        E1=Entry(self.tk,width=300)
        E1.pack()
        self.entry=E1
        self.display_label=Label(self.tk, text="")
        self.display_label.pack() 
        Button(self.tk,text='執行',command=self.run).pack()
        Button(self.tk,text='顯示所有學生',command=partial(self.insert_tv,"select * from student")).pack()
        Button(self.tk,text='顯示所有老師',command=partial(self.insert_tv,"select * from teacher")).pack()
        Button(self.tk,text='顯示所有課室',command=partial(self.insert_tv,"select * from class")).pack()
        Button(self.tk,text='顯示所有社團',command=partial(self.insert_tv,"select * from club")).pack()
        Button(self.tk,text='顯示所有已借出的書',command=partial(self.insert_tv,"select * from book")).pack()

    def comfirm(self):
        self.entry.delete(0,END)
        if(self.combo.get()=="INSERT"):
            self.entry.insert(0,"insert into (table) values()")
        elif(self.combo.get()=="SELECT-FROM-WHERE"):
            self.entry.insert(0,"select (attribute) from (table) where (condition)")
        elif(self.combo.get()=="UPDATE"):
            self.entry.insert(0,"update (table) set () where (condition)")
        elif(self.combo.get()=="DELETE"):
            self.entry.insert(0,"delete from (table) where (condition)")
            
    def run(self):
        self.display_label.config(text=self.entry.get())
        if(self.combo.get()=="SELECT-FROM-WHERE"):
            self.insert_tv(self.entry.get())  
        else:
            try:
              self.sql.input_commend(self.entry.get())
            except:
              self.display_label.config(text="發生錯誤！")

        
    def insert_tv(self,instruction):
            #清空tree、checkbutton
        items = self.tv.get_children()
        [self.tv.delete(item) for item in items]
        self.tv.update()
        for child in self.button_frame.winfo_children()[1:]: #第一个构件是label，所以忽略
            child.destroy()
        #重设tree、button对应关系
        self.orm={}
        list = self.sql.show(instruction)
        
        for i in range(len(list)):
            self.tv.insert('', i, value=list[i],tags=('oddrow'))#item默认状态tags
        #更新canvas的高度
        height = (len(self.tv.get_children()) + 1) * self.rowheight  # treeview实际高度
        self.canvas.itemconfigure(self.tv_frame, height=height) #设定窗口tv_frame的高度
        self.tk.update()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))#滚动指定的范围
 
    def create_tv(self):
        #放置 canvas、滚动条的frame
        canvas_frame=Frame(self.tk,width=600,height=400)
        canvas_frame.pack(fill=X)
 
        #只剩Canvas可以放置treeview和按钮，并且跟滚动条配合
        self.canvas=Canvas(canvas_frame,width=500,height=500,scrollregion=(0,0,500,400))
        self.canvas.pack(side=LEFT,fill=BOTH,expand=1)
        #滚动条
        ysb = Scrollbar(canvas_frame, orient=VERTICAL, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=ysb.set)
        ysb.pack(side=RIGHT, fill=Y)
        #!!!!=======重点：鼠标滚轮滚动时，改变的页面是canvas 而不是treeview
        self.canvas.bind_all("<MouseWheel>",lambda event:self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))
 
 
        #想要滚动条起效，得在canvas创建一个windows(frame)！！
        tv_frame=Frame(self.canvas)
        self.tv_frame=self.canvas.create_window(0, 0, window=tv_frame, anchor='nw',width=600,height=400)#anchor该窗口在左上方
 
        #放置button的frame
        self.button_frame=Frame(tv_frame)
        self.button_frame.pack(side=LEFT, fill=Y)
        Label(self.button_frame,width=3).pack()  #填充用
 
 
        #创建treeview
        self.tv = Treeview(tv_frame, height=10, columns=self.columns, show='headings')#height好像设定不了行数，实际由插入的行数决定
        self.tv.pack(expand=1, side=LEFT, fill=BOTH)
        #设定每一列的属性
        for i in range(len(self.columns)):
            self.tv.column(self.columns[i], width=0, minwidth=self.widths[i], anchor='center', stretch=True)
 
 
        #设定treeview格式
        # import tkinter.font as tkFont
        # ft = tkFont.Font(family='Fixdsys', size=20, weight=tkFont.BOLD)
        self.tv.tag_configure('oddrow', font='Arial 12')                    #设定treeview里字体格式font=ft
        self.tv.tag_configure('select', background='SkyBlue',font='Arial 12')#当对应的按钮被打勾，那么对于的行背景颜色改变！
        self.rowheight=27                                       #很蛋疼，好像tkinter里只能用整数！
        Style().configure('Treeview', rowheight=self.rowheight)      #设定每一行的高度

 
 
   
    

from sql import sql_connecter

if __name__=="__main__":
  sql=sql_connecter()
  sql.create_database("sql_tutorial")
  sql.use_database()
  sql.drop_table("student")
  sql.drop_table("teacher")
  sql.drop_table("class")
  sql.drop_table("book")
  sql.drop_table("club")
  sql.create_table("student","student_id varchar(20) primary key,student_name varchar(20),class varchar(20),club varchar(20)")

  with open("student.csv", "r") as f:
    reader = csv.reader(f,delimiter=",")
    for i, line in enumerate(reader):
        if i>0:
          str=""
          for j in line:
              str+="'"
              str+=j
              str+="'"
              str+=","
          str=str[:-1]
          sql.insert_table("student",str)
  
  sql.create_table("teacher","teacher_id varchar(20) primary key,teacher_name varchar(20),major varchar(20)")
  
  with open("teacher.csv", "r") as f:
    reader = csv.reader(f,delimiter=",")
    for i, line in enumerate(reader):
        if i>0:
          str=""
          for j in line:
              str+="'"
              str+=j
              str+="'"
              str+=","
          str=str[:-1]
          sql.insert_table("teacher",str)
  sql.create_table("class","class_name varchar(20) primary key,main_teacher_id varchar(20),class_major varchar(20)")
  with open("class.csv", "r") as f:
    reader = csv.reader(f,delimiter=",")
    for i, line in enumerate(reader):
        if i>0:
          str=""
          for j in line:
              str+="'"
              str+=j
              str+="'"
              str+=","
          str=str[:-1]
          sql.insert_table("class",str)
  sql.create_table("club","club_name varchar(20) primary key,main_teacher_id varchar(20),category varchar(20)")
  with open("club.csv", "r") as f:
    reader = csv.reader(f,delimiter=",")
    for i, line in enumerate(reader):
        if i>0:
          str=""
          for j in line:
              str+="'"
              str+=j
              str+="'"
              str+=","
          str=str[:-1]
          sql.insert_table("club",str)
  sql.create_table("book","book_name varchar(20) primary key,id varchar(20),borrow_time varchar(20)")
  with open("book.csv", "r") as f:
    reader = csv.reader(f,delimiter=",")
    for i, line in enumerate(reader):
        if i>0:
          str=""
          for j in line:
              str+="'"
              str+=j
              str+="'"
              str+=","
          str=str[:-1]
          sql.insert_table("book",str)
  My_Tk(sql)
  sql.close()