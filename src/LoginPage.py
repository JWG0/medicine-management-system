from tkinter import *
from tkinter.messagebox import *
from MainPage import *
from database import *
class LoginPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        # 设置窗口大小,与出现的位置距离窗体左上角(+100+100)
        self.root.geometry('%dx%d+%d+%d' % (300, 200,400,300))
        # 图标
        try:
            self.root.iconbitmap("./drug_manage.ico")
        except:
            pass
        # 设置背景色
        self.root["background"] = "#f0f0f0"
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 创建Frame,框架
        self.page.pack()#显示Frame
        Label(self.page).grid(row=0, stick=W)#stick=W表示左对齐,tick=E表示右对齐,默认居中
        Label(self.page, text='账户: ').grid(row=1, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1,padx=10)
        self.username.set('root')

        Label(self.page, text='密码: ').grid(row=2, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1,padx=10)
        self.password.set('123456')
        #行号和列号并不是像在坐标轴上一样严格，只是代表一个上下左右的关系
        Button(self.page, text='登陆', command=self.loginCheck).grid(
            row=3, column=0, ipady=10,ipadx=30)
        Button(self.page, text='退出', command=self.page.quit).grid(
            row=3, column=1, ipady=10,ipadx=30,stick=E)

    def loginCheck(self):
        name = self.username.get()
        secret = self.password.get()
        #跳转到database.py连接数据库
        if name_password(name,secret)==True:
            self.page.destroy()
            MainPage(self.root)
            # showinfo(title='提示', message='数据库连接成功！')
        else:
            showinfo(title='错误', message='数据库连接失败!\n账号或密码错误！')
