import tkinter
from tkinter import Y, ttk


 
win = tkinter.Tk()
win.title("win")
win.geometry("620x400+10+20")

frame=tkinter.Frame(win)
# 创建表格
tree = ttk.Treeview(frame,selectmode="browse")


# 定义列
tree['columns'] = ['name','age','weight','number']
tree.pack()

vsb = ttk.Scrollbar(win, orient="vertical", command=tree.yview)
vsb.place(x=600, y=0, height=400)
tree.configure(yscrollcommand=vsb.set)

# 设置列宽度
tree.column('name',width=100)
tree.column('age',width=100)
tree.column('weight',width=100)
tree.column('number',width=100)

# 添加列名
tree.heading('name',text='姓名')
tree.heading('age',text='年龄')
tree.heading('weight',text='体重')
tree.heading('number',text='工号')

frame.grid(row=0)
# 第一个参数为第一层级，可能在这不太好理解，下篇文章中说到树状结构就理解了

win.mainloop()
