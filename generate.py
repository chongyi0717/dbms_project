
from numpy import diff


def generate():
    from unicodedata import category
    from faker import Faker
    import numpy as np
    import pandas as pd
    import random
    import datetime
    fake = Faker("zh_CN")
    name=[fake.name() for i in range(0,100)]
    id=random.sample(range(100000,999999),100)
    buff=[]
    for i in id:
        i="F"+str(i)
        buff.append(i)
    id=buff
    list=[]
    for i in range(100):
        list.append("")
    list=["S1C1","S1C2","S1C3","S2S1","S2S2","S3C1","S3C2","S3S1","S3S2","S3S3"]
    buff=list
    class_list=[]
    for i in range(100):
        class_list.append(random.choice(list))
    list=["弦樂團","管樂團","華樂團","棋社","動畫社","漫畫社","撞球社","自行車社","學生會","爵士社"]
    club_list=[]
    for i in range(100):
        club_list.append(random.choice(list))
    dict={
        "student_id":id,
        "student_name":name,
        "class":class_list,
        "club":club_list
    }
    dict=pd.DataFrame(dict)
    dict.to_csv("student.csv",encoding="gbk",index=False)
    student_id=id
    class_list=buff

    name=[fake.name() for i in range(0,20)]
    id=random.sample(range(100000,999999),20)
    buff=[]
    for i in id:
        i="A"+str(i)
        buff.append(i)
    id=buff


    list=["中文","英文","化學","電腦"]
    major_list=[]
    for i in range(20):
        major_list.append(random.choice(list))
    dict={
        "teacher_id":id,
        "teacher_name":name,
        "major":major_list
    }
    dict=pd.DataFrame(dict)
    dict.to_csv("teacher.csv",encoding="gbk",index=False)
    teacher_id=id

    main_teacher_name=[]
    for i in class_list:
        main_teacher_name.append(random.choice(name))
    major_list=[]
    for i in class_list:
        if i[2]=='C':
            major_list.append("商科")
        elif i[2]=='S':
            major_list.append("理科")
    dict={
        "class_name":class_list,
        "main_teacher_name":main_teacher_name,
        "major":major_list
    }
    dict=pd.DataFrame(dict)
    dict.to_csv("class.csv",encoding="gbk",index=False)

    club_list=["弦樂團","管樂團","華樂團","棋社","動畫社","漫畫社","撞球社","自行車社","合唱團","爵士社"]
    category_list=["康樂","康樂","康樂","學藝","學藝","學藝","運動","運動","康樂","康樂"]
    main_teacher_name=[]
    for i in club_list:
        main_teacher_name.append(random.choice(name))
    dict={
        "club":club_list,
        "main_teacher_name":main_teacher_name,
        "category":category_list
    }
    dict=pd.DataFrame(dict)
    dict.to_csv("club.csv",encoding="gbk",index=False)

    df=pd.read_csv("Books.csv",encoding="gbk",low_memory=False)
    book_name=df["Book-Title"][0:500]
    buff=[]
    book_name=set(book_name)
    for i in book_name:
        if(len(i)<=20 and "'" not in i):
            buff.append(i)
    book_name=buff
    id=teacher_id+student_id+['None']
    buff=[]
    for i in book_name:
        buff.append(random.choice(id))
    id=buff
    import time
    a1=(2022,1,1,0,0,0,0,0,0) 
    a2=(2022,5,30,23,59,59,0,0,0) 
    start=time.mktime(a1) 
    end=time.mktime(a2) 
    date_list=[]
    different=[]
    price=[]
    for i in range(len(book_name)):
        t=random.randint(start,end) 
        date_touple=time.localtime(t) 
        d1=datetime.datetime(date_touple.tm_year,date_touple.tm_mon,date_touple.tm_mday)
        d2=datetime.datetime.today()
        date=time.strftime("%Y/%m/%d",date_touple) 
        if id[i]!='None':
            different.append((d2-d1).days)
            date_list.append(date)
            price.append(random.randint(300,1000))
        else:
            date_list.append('None')
            different.append('None')
            price.append(0)
    dict={
        "book_name":book_name,
        "id":id,
        "borrow_time":date_list,
        "price":price,
        "different":different
    }
    dict=pd.DataFrame(dict)
    dict.to_csv("book.csv",encoding="gbk",index=False)
def modify_book():
    import pandas as pd
    import datetime
    df=pd.read_csv("book.csv",encoding="gbk")
    different=[]
    for i in df["borrow_time"]:
        try:
            d1 = datetime.datetime.strptime(i, '%Y/%m/%d')
            d2=datetime.datetime.today()
            different.append((d2-d1).days)
        except:
            different.append('None')
    dict={
        "book_name":df["book_name"],
        "id":df["id"],
        "borrow_time":df["borrow_time"],
        "price":df["price"],
        "different":different
        
    }
    dict=pd.DataFrame(dict)
    dict.to_csv("book.csv",encoding="gbk",index=False)
generate()