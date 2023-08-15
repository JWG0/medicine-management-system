from tkinter import *
from view_insert import *  # 菜单栏对应的各个子页面
from view_delete import *
from view_select import *
from view_update import *
from view_server import *
from LoginPage import *

class MainPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d+%d+%d' % (785, 450,400,300))  # 设置窗口大小
        self.createPage()

    def createPage(self):
        self.serverPage = ServerFrame(self.root)
        self.insertPage = InsertFrame(self.root)  # 创建不同Frame,框架
        self.deletePage = DeleteFrame(self.root)
        self.updatePage = UpdateFrame(self.root)
        self.selectPage = SelectFrame(self.root)
        self.insertPage.pack()  # 默认显示数据录入界面
        menubar = Menu(self.root)
        menubar.add_command(label='  功能服务  ', command=self.server)
        menubar.add_command(label='  添加数据  ', command=self.insertData)
        menubar.add_command(label='  删除数据  ', command=self.deleteData)
        menubar.add_command(label='  修改数据  ', command=self.updateData)
        menubar.add_command(label='  查询数据  ', command=self.selectData)
        self.root['menu'] = menubar  # 设置菜单栏


    def server(self):
        self.serverPage.pack()
        self.insertPage.pack_forget()
        self.deletePage.pack_forget()
        self.updatePage.pack_forget()
        self.selectPage.pack_forget()

    def insertData(self):
        self.serverPage.pack_forget()
        self.insertPage.pack()
        self.deletePage.pack_forget()
        self.updatePage.pack_forget()
        self.selectPage.pack_forget()

    def deleteData(self):
        self.serverPage.pack_forget()
        self.insertPage.pack_forget()
        self.deletePage.pack()
        self.updatePage.pack_forget()
        self.selectPage.pack_forget()

    def updateData(self):
        self.serverPage.pack_forget()
        self.insertPage.pack_forget()
        self.deletePage.pack_forget()
        self.updatePage.pack()
        self.selectPage.pack_forget()

    def selectData(self):
        self.serverPage.pack_forget()
        self.insertPage.pack_forget()
        self.deletePage.pack_forget()
        self.updatePage.pack_forget()
        self.selectPage.pack()

