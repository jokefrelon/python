import re
import webbrowser
import tkinter.messagebox
import uuid
from tkinter import *
from tkinter import ttk

import pymysql
import requests
from lxml import etree

# 初始化pymysql的连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='llll',
                     database='website')
cursor = db.cursor()


# 向数据库里面插入数据
def insert1(link, title, content):
    sql = "insert into link (uuid, link, title, content) values  ('%s', '%s',  '%s', '%s' )" % (
        uuid.uuid4(), link, title, content)

    try:
        db.ping(reconnect=True)
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print("插入数据错误")
        db.close()


# 向数据库里面插入数据
def insert2(name, link, title, content):
    sql = "insert into link (uuid, name, link, title, content) values  ('%s', '%s',  '%s', '%s', '%s' )" % (
        uuid.uuid4(), name, link, title, content)

    try:
        db.ping(reconnect=True)
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print("插入数据错误")
        db.close()


# 从数据库中删除元素
def delByUUID(struid):
    sql = "delete from `link` where `uuid` = '%s'" % struid
    res = 0
    try:
        db.ping(reconnect=True)
        res = cursor.execute(sql)
        db.commit()
        return res
    except:
        db.rollback()
        print("删除数据错误")
        db.close()
        return res


# 更新记录
def updateFavorByUUID(struid, intfavor):
    sql = "update `link` set `favor` = '%s' where `uuid` = '%s'" % (intfavor, struid)
    res = 0
    try:
        db.ping(reconnect=True)
        res = cursor.execute(sql)
        db.commit()
        return res
    except:
        db.rollback()
        print("更新数据错误")
        db.close()
        return res


# 从数据库获取数据
def getData():
    sql = """select * from link"""
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        gp = []
        for er in results:
            tmp = {'uuid': er[0], 'link': er[1], 'name': er[2], 'title': er[3],
                   'content': er[4],
                   'favor': er[5],
                   'isdel': er[6]}
            gp.append(tmp)
        return gp
    except:
        print("Error: unable to fetch data")
    db.close()


def getFavorData():
    sql = """select * from link where favor = '1'"""
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        gp = []
        for er in results:
            tmp = {'uuid': er[0], 'link': er[1], 'name': er[2], 'title': er[3],
                   'content': er[4],
                   'favor': er[5],
                   'isdel': er[6]}
            gp.append(tmp)
        return gp
    except:
        print("Error: unable to fetch data")
    db.close()


class mytk(Tk):
    def __init__(self):
        super().__init__()

        # 样式
        self.style = None

        # 所有的界面frame
        self.frame4 = None  # 收藏界面
        self.frame3 = None  # 查看界面
        self.frame2 = None  # 添加界面
        self.frame1 = None  # main 界面

        # main界面的控件 添加到frame1
        self.Label5 = None
        self.Label4 = None
        self.Label3 = None
        self.Label2 = None
        self.Label1 = None

        # 添加界面的控件， 添加到frame2
        self.add_button2 = None
        self.add_button1 = None
        self.add_entry2 = None
        self.add_label2 = None
        self.add_label1 = None
        self.add_entry1 = None

        # 查看界面的控件，添加到frame3
        self.all_scrollBar = None
        self.all_tree = None
        self.all_frame = None
        self.all_button_open = None
        self.all_button_delete = None
        self.all_button_favor = None
        self.all_button_back = None

        # 收藏界面控件添加到 frame4
        self.favor_scrollBar = None
        self.favor_tree = None
        self.favor_frame = None
        self.favor_button_open = None
        self.favor_button_unfavor = None
        self.favor_button_back = None

        self.title('网页链接管理系统')
        self.geometry("300x430+100+100")
        self.resizable(False, False)
        self.iconbitmap("avatars-02_Nemo.ico")
        self.setupUI()

    # 设置并初始化基础UI控件
    def setupUI(self):
        self.frame1 = Frame(self)  # main界面，运行就是这个界面
        self.frame2 = Frame(self)  # 添加界面，点击添加后显示的界面
        self.frame3 = Frame(self)  # 显示所有的链接，点击查看后显示的界面
        self.frame4 = Frame(self)  # favor界面，点击收藏后显示的界面

        # 添加按钮 设置样式
        self.Label1 = Button(self.frame1, text='添加', width=10, height=2,
                             activebackground="#aaa", activeforeground="#000", command=self.showadd)
        self.Label2 = Button(self.frame1, text='查看', width=10, height=2,
                             activebackground="#aaa", activeforeground="#000", command=self.showall)
        self.Label3 = Button(self.frame1, text='收藏', width=10, height=2,
                             activebackground="#aaa", activeforeground="#000", command=self.showfavor)
        self.Label5 = Button(self.frame1, text='关于', width=10, height=2,
                             activebackground="#aaa", activeforeground="#000", command=self.showabout)
        self.Label4 = Button(self.frame1, text='退出', width=10, height=2,
                             activebackground="#aaa", activeforeground="#000", command=self.destroy)
        # 给控件布局
        self.Label1.pack(pady=[20, 20])
        self.Label2.pack(pady=[20, 20])
        self.Label3.pack(pady=[20, 20])
        self.Label5.pack(pady=[20, 20])
        self.Label4.pack(pady=[20, 20])

        self.frame1.pack(fill=BOTH, anchor=CENTER, expand=True, side=TOP)

        # 调用下面的函数 初始化别的界面需要用到的控件
        self.init_add()
        self.init_all()
        self.init_favor()

    # 隐藏别的界面，显示 [主](main){逻辑上的,其实对应 frame1 } 界面
    def back2main(self):
        self.geometry("300x430")

        # 隐藏别的界面, 仅显示当前[主](main){逻辑上的,其实对应 frame1 } 界面
        self.frame2.pack_forget()
        self.frame3.pack_forget()
        self.frame4.pack_forget()

        self.frame1.pack(fill=BOTH, anchor=CENTER, expand=True, side=TOP)

    # 初始化 [添加](add) 界面所需要的控件
    def init_add(self):
        self.add_label1 = Label(self.frame2, text="网址：")
        self.add_entry1 = Entry(self.frame2, width=22, font=("微软雅黑", 14), textvariable=StringVar())

        self.add_label2 = Label(self.frame2, text="名称：")
        self.add_entry2 = Entry(self.frame2, width=22, font=("微软雅黑", 14), textvariable=StringVar())

        self.add_button1 = Button(self.frame2, text="保存",  width=10, height=2,
                                  activebackground="#aaa", activeforeground="#000", command=self.getweb)
        self.add_button2 = Button(self.frame2, text="返回", width=10, height=2,
                                  activebackground="#aaa", activeforeground="#000", command=self.back2main)

    # 设置[添加](add)界面的布局
    def layout_add(self):
        self.add_label2.place(x=5, y=150)
        self.add_entry2.place(x=45, y=150)

        self.add_label1.place(x=5, y=75)
        self.add_entry1.place(x=45, y=75)

        self.add_button1.place(x=50, y=250)
        self.add_button2.place(x=180, y=250)

        self.frame2.pack(fill=BOTH, anchor=CENTER, expand=True, side=TOP)

    # 显示[添加](add)界面
    def showadd(self):
        self.frame1.pack_forget()
        self.frame3.pack_forget()
        self.frame4.pack_forget()

        self.layout_add()

    # 初始化 [查看](favor) 界面所需要的所有的控件,并设置控件样式
    def init_all(self):
        self.all_scrollBar = Scrollbar(self.frame3)

        self.style = ttk.Style(self)
        self.style.configure("all.Treeview")

        self.all_tree = ttk.Treeview(self.frame3,
                                     columns=('c1', 'c2', 'c3', 'c4', 'c5'),
                                     show="headings",
                                     style="all.Treeview",
                                     yscrollcommand=self.all_scrollBar.set)

        # 设置每列宽度和对齐方式
        self.all_tree.column('c1', width=100, anchor='center')
        self.all_tree.column('c2', width=150, anchor='center')
        self.all_tree.column('c3', width=200, anchor='center')
        self.all_tree.column('c4', width=490, anchor='center')
        self.all_tree.column('c5', width=40, anchor='center')

        # 设置每列表头标题文本
        self.all_tree.heading('c1', text='名称')
        self.all_tree.heading('c2', text='链接')
        self.all_tree.heading('c3', text='标题')
        self.all_tree.heading('c4', text='内容')
        self.all_tree.heading('c5', text='收藏')

        # Treeview组件与垂直滚动条结合
        self.all_scrollBar.config(command=self.all_tree.yview)

        self.all_frame = Frame(self.frame3, bg="#ddd")

        # 定义按键
        self.all_button_open = Button(self.all_frame, text="打开", width=10, height=2, bg="#fff", fg="#000",
                                      activebackground="#aaa", activeforeground="#000", command=self.all_openurl)
        self.all_button_favor = Button(self.all_frame, text="收藏", width=10, height=2, bg="#fff", fg="green",
                                       activebackground="#aaa", activeforeground="#1a1", command=self.all_setItFavor)
        self.all_button_delete = Button(self.all_frame, text="删除", width=10, height=2, bg="#fff", fg="#910",
                                        activebackground="#aaa", activeforeground="red", command=self.all_getSelect)
        self.all_button_back = Button(self.all_frame, text="返回", width=10, height=2, bg="#fff", fg="#000",
                                      activebackground="#aaa", activeforeground="#000", command=self.back2main)
        self.layout_all()

    # [查看](all) 界面的布局(与favor类似)
    def layout_all(self):
        self.all_scrollBar.pack(side=RIGHT, fill=Y)

        self.all_button_open.pack(side=LEFT, padx=[100, 0], pady=5)
        self.all_button_favor.pack(side=LEFT, padx=[150, 0], pady=5)
        self.all_button_delete.pack(side=LEFT, padx=[150, 0], pady=5)
        self.all_button_back.pack(side=RIGHT, padx=[0, 100], pady=5)

        self.all_frame.pack(side=BOTTOM, fill=X)
        self.all_tree.pack(side=LEFT, fill=Y)
        self.frame3.pack(fill=BOTH, anchor=CENTER, expand=True, side=TOP)

    # 显示[查看](all)界面，主要是重新设置大小，恢复pack
    def showall(self):
        # 设置长宽
        self.geometry("1000x430")

        # 隐藏别的选项界面
        self.frame1.pack_forget()
        self.frame2.pack_forget()
        self.frame4.pack_forget()

        # 调用布局函数
        self.layout_all()

        # 调用定义的函数处理数据
        self.all_del_Item_From_Tree()
        self.all_insert_Data_2_Tree()

    # 初始化 [收藏](favor) 界面需要的控件
    def init_favor(self):
        self.favor_scrollBar = Scrollbar(self.frame4)

        self.style = ttk.Style(self)
        self.style.configure("favor.Treeview")

        self.favor_tree = ttk.Treeview(self.frame4,
                                       columns=('co1', 'co2', 'co3', 'co4'),
                                       show="headings",
                                       style="favor.Treeview",
                                       yscrollcommand=self.favor_scrollBar.set)

        # 设置每列宽度和对齐方式
        self.favor_tree.column('co1', width=100, anchor='center')
        self.favor_tree.column('co2', width=150, anchor='center')
        self.favor_tree.column('co3', width=200, anchor='center')
        self.favor_tree.column('co4', width=550, anchor='center')

        # 设置每列表头标题文本
        self.favor_tree.heading('co1', text='名称')
        self.favor_tree.heading('co2', text='链接')
        self.favor_tree.heading('co3', text='标题')
        self.favor_tree.heading('co4', text='内容')

        # Treeview组件与垂直滚动条结合
        self.favor_scrollBar.config(command=self.favor_tree.yview)

        self.favor_frame = Frame(self.frame4, bg="#ddd")

        # 定义按键
        self.favor_button_open = Button(self.favor_frame, text="打开", width=10, height=2, bg="#fff", fg="#000",
                                        activebackground="#aaa", activeforeground="#000", command=self.favor_openurl)

        self.favor_button_unfavor = Button(self.favor_frame, text="取消收藏", width=10, height=2, bg="#fff", fg="red",
                                           activebackground="#aaa", activeforeground="#f11",
                                           command=self.favor_setItUnfavor)

        self.favor_button_back = Button(self.favor_frame, text="返回", width=10, height=2, bg="#fff", fg="#000",
                                        activebackground="#aaa", activeforeground="#000", command=self.back2main)
        # 利用函数来设置布局
        self.layout_favor()

    # [收藏](favor) 界面的布局
    def layout_favor(self):
        self.favor_button_open.pack(side=LEFT, padx=[300, 0], pady=5)
        self.favor_button_unfavor.pack(side=LEFT, padx=[80, 0], pady=5)
        self.favor_button_back.pack(side=RIGHT, padx=[0, 300], pady=5)

        self.favor_frame.pack(side=BOTTOM, fill=X)
        self.favor_tree.pack(side=LEFT, fill=Y)
        self.favor_scrollBar.pack(side=RIGHT, fill=Y)
        self.frame4.pack(fill=BOTH, anchor=CENTER, expand=True, side=TOP)

    # 显示 [收藏](favor)界面
    def showfavor(self):
        # 设置长宽
        self.geometry("1000x430")

        # 隐藏别的选项界面
        self.frame1.pack_forget()
        self.frame2.pack_forget()
        self.frame3.pack_forget()

        # 调用布局函数
        self.layout_favor()

        # 调用定义的函数处理数据
        self.favor_del_Item_From_Tree()
        self.favor_insert_Data_2_Tree()

    # 获取用户输入的链接，请求该链接获取 title content
    def getweb(self):
        link = self.add_entry1.get()
        that_name = self.add_entry2.get()

        if link != "" and re.match(r"((?:https?:)?\/\/(?:[\w]+[.][\w]+)+/?)+$", link) is not None:
            webPage = requests.get(
                url=self.add_entry1.get(),
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
                },
                timeout=5
            )
            html = webPage.text
            eroot = etree.HTML(html)
            title = None
            content = None
            try:
                title = eroot.xpath('//head/title/text()')[0]
                content = eroot.xpath('//meta[@name="description"]/@content')[0]
                tkinter.messagebox.showinfo(title="保存成功", message="保存成功")

                if that_name == "" or that_name == " ":
                    insert1(link, title, content)
                else:
                    insert2(that_name, link, title, content)
            except:
                if that_name == "" or that_name == " ":
                    insert1(link, title, content)
                else:
                    insert2(that_name, link, title, content)
                tkinter.messagebox.showwarning(title="警告⚠",
                                               message="目标网站不支持title或description，但已保存相关内容为空")
        else:
            tkinter.messagebox.showerror(title="链接错误", message="输入的链接错误，程序无法处理")

    # 清空 [查看](all)界面 Treeview里column的数据
    def all_del_Item_From_Tree(self):
        for item in self.all_tree.get_children():
            self.all_tree.delete(item)

    # 清空 [收藏](favor)界面 Treeview里column的数据
    def favor_del_Item_From_Tree(self):
        try:
            for item in self.favor_tree.get_children():
                self.favor_tree.delete(item)
        except:
            print("删除元素失败")

    # 把数据库查询到的数据显示到 [查看](all) 界面上
    def all_insert_Data_2_Tree(self):
        for er in getData():
            thatuid = er['uuid']
            name = er['name']
            link = er['link']
            title = er['title']
            content = er['content']
            favor = er['favor']

            name = name if name is not None else "未命名"
            title = title if title is not None else "无标题"
            content = content if content is not None else "无内容"
            favor = "✔" if favor == 1 else "❌"

            self.all_tree.insert("", index=END, text=thatuid, values=(name, link, title, content, favor))

    # 把数据库查询到的 [收藏](favor)的数据显示到页面上
    def favor_insert_Data_2_Tree(self):
        for er in getFavorData():
            thatuid = er['uuid']
            name = er['name']
            link = er['link']
            title = er['title']
            content = er['content']

            name = name if name is not None else "未命名"
            title = title if title is not None else "无标题"
            content = content if content is not None else "无内容"

            self.favor_tree.insert("", index=END, text=thatuid, values=(name, link, title, content))

    # [查看](all)界面 删除按钮的功能 => 删除数据
    def all_getSelect(self):
        if len(self.all_tree.selection()) != 0:
            thatuid = self.all_tree.item(self.all_tree.selection())["text"]

            if delByUUID(thatuid) == 1:
                self.all_tree.delete(self.all_tree.selection())
                tkinter.messagebox.showinfo(title="成功✔", message="删除数据成功！")
            else:
                tkinter.messagebox.showerror(title="错误❌", message="后台处理数据错误，请联系管理员处理")
        else:
            tkinter.messagebox.showwarning(title="警告⚠", message="请先选择后，再删除")

    # [查看](all)界面 收藏操作
    def all_setItFavor(self):
        if len(self.all_tree.selection()) != 0:
            thatuid = self.all_tree.item(self.all_tree.selection())["text"]
            for er in getData():
                if thatuid == er['uuid']:  # 从所有的数据中获取与当前选择项目匹配的数据
                    if er['favor'] == 0:  # 判断是否已经收藏
                        if updateFavorByUUID(thatuid, 1) == 1:  # 判断数据库返回值来确认是否更新成功
                            self.all_tree.set(self.all_tree.selection(), column='c5', value="✔")
                            tkinter.messagebox.showinfo(title="收藏成功✔", message="已收藏该网站！")
                        else:
                            tkinter.messagebox.showerror(title="错误❌", message="后台处理数据错误，请联系管理员处理")
                    else:
                        tkinter.messagebox.showinfo(title="提示", message="已收藏该网站！请勿重复收藏。")
        else:
            tkinter.messagebox.showwarning(title="警告⚠", message="请先选择后，再删除")

    # [收藏](favor)界面 取消收藏操作
    def favor_setItUnfavor(self):
        if len(self.favor_tree.selection()) != 0:
            thatuid = self.favor_tree.item(self.favor_tree.selection())["text"]
            for er in getData():
                if thatuid == er['uuid']:  # 从所有的数据中获取与当前选择项目匹配的数据
                    if updateFavorByUUID(thatuid, 0) == 1:  # 判断数据库返回值来确认是否更新成功
                        self.favor_tree.delete(self.favor_tree.selection())
                        tkinter.messagebox.showinfo(title="取消成功✔", message="已取消收藏该网站！")
                    else:
                        tkinter.messagebox.showerror(title="错误❌", message="后台处理数据错误，请联系管理员处理")
        else:
            tkinter.messagebox.showwarning(title="警告⚠", message="请先选择后，再删除")

    # [查看](all)界面 打开link操作
    def all_openurl(self):
        if len(self.all_tree.selection()) != 0:
            link = self.all_tree.item(self.all_tree.selection())['values'][1]
            webbrowser.open(link)
        else:
            tkinter.messagebox.showwarning(title="警告⚠", message="请先选择要打开的网站")

    # [收藏](favor)界面打开link操作
    def favor_openurl(self):
        if len(self.favor_tree.selection()) != 0:
            link = self.favor_tree.item(self.favor_tree.selection())['values'][1]
            webbrowser.open(link)
        else:
            tkinter.messagebox.showwarning(title="警告⚠", message="请先选择要打开的网站")

    def showabout(self):
        tkinter.messagebox.showinfo(title="关于", message="本程序由李明 周旭 曹淼淼共同制作！")


if __name__ == '__main__':
    mytk().mainloop()

# 思路调整 ！ tk不可能渲染出来 scroll的frame，那就分好几个页面来做增删改查工作。
# 添加 - 查看 - 收藏 - 退出
#
# 添加：获取用户输入，调用request，获取title，content，保存到数据库
# 查看：treeview => name , link ，title , content
# 收藏：也是一种展示
