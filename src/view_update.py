from tkinter import *
from tkinter.messagebox import *
from LoginPage import *
from database import *

class UpdateFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.row = 0  # 定义类变量
        self.column = 2
        self.width=10
        self.color='#ffff99'
        self.root = master  # 定义内部变量root
        self.drug_no_before=StringVar()
        self.drug_no = StringVar()
        self.drug_name = StringVar()
        self.drug_level = StringVar()
        self.drug_price=StringVar()

        self.employee_no_before = StringVar()
        self.employee_no = StringVar()
        self.employee_name = StringVar()
        self.employee_age = StringVar()
        self.employee_sex = StringVar()
        self.employee_date = StringVar()

        self.supplier_no_before = StringVar()
        self.supplier_no = StringVar()
        self.supplier_name = StringVar()
        self.supplier_city = StringVar()

        self.customer_no_before = StringVar()
        self.customer_no = StringVar()
        self.customer_name = StringVar()
        self.customer_city = StringVar()

        self.warehouse_no_before = StringVar()
        self.warehouse_no = StringVar()
        self.warehouse_name = StringVar()
        self.warehouse_employee_no = StringVar()
        self.warehouse_sum = StringVar()

        self.createPage()

    def createPage(self):
        Label(self, text='更新药品').grid(row=1, column=0)
        Label(self, text='更新前药品号：',bg=self.color).grid(row=1, column=self.column)
        Entry(self, textvariable=self.drug_no_before,bg=self.color).grid(row=1, column=self.column+2,padx=5)
        self.row = 2
        Label(self, text='更新为：').grid(row=self.row, column=0)
        Label(self, text='药品号：').grid(row=self.row, column=1)
        Entry(self, textvariable=self.drug_no).grid(row=self.row, column=2, padx=5)
        # self.drug_no.set('0001')
        Label(self, text='药品名: ').grid(row=self.row, column=3)
        Entry(self, textvariable=self.drug_name).grid(row=self.row, column=4, padx=5)
        # self.drug_name.set('布洛芬')
        Label(self, text='药品级别: ').grid(row=self.row, column=5)
        Entry(self, textvariable=self.drug_level).grid(row=self.row, column=6, padx=5)
        # self.drug_level.set('A/B/C')
        self.row = 3
        Label(self, text='药品单价: ').grid(row=self.row, column=1)
        Entry(self, textvariable=self.drug_price).grid(row=self.row, column=2, padx=5)
        Button(self, text='更新', command=self.command_update_drug).grid(row=self.row, column=8, padx=5)

        Label(self, text='更新员工').grid(row=4, column=0, ipady=10)
        Label(self, text='更新前员工号：',bg=self.color).grid(row=4, column=self.column)
        Entry(self, textvariable=self.employee_no_before,bg=self.color).grid(row=4, column=self.column+2, padx=5)
        self.row = 5
        Label(self, text='更新为：').grid(row=self.row, column=0)
        Label(self, text='员工号：').grid(row=self.row, column=1)
        Entry(self, textvariable=self.employee_no).grid(row=self.row, column=2, padx=5)
        # self.employee_no.set('20220001')
        Label(self, text='员工名: ').grid(row=self.row, column=3)
        Entry(self, textvariable=self.employee_name).grid(row=self.row, column=4, padx=5)
        # self.employee_name.set('张三')
        Label(self, text='员工年龄: ').grid(row=self.row, column=5)
        Entry(self, textvariable=self.employee_age).grid(row=self.row, column=6, padx=5)
        # self.employee_age.set('34')
        self.row = 6
        Label(self, text='员工性别: ').grid(row=self.row, column=1)
        Entry(self, textvariable=self.employee_sex).grid(row=self.row, column=2, padx=5)
        # self.employee_sex.set('男')
        Label(self, text='入职日期: ').grid(row=self.row, column=3)
        Entry(self, textvariable=self.employee_date).grid(row=self.row, column=4, padx=5)
        # self.employee_date.set('' + str(now_date))  # 当前日期
        Button(self, text='更新', command=self.command_update_employee).grid(row=self.row, column=8, padx=5)

        Label(self, text='更新供应商').grid(row=7, column=0)
        Label(self, text='更新前供应商号：',bg=self.color).grid(row=7, column=self.column)
        Entry(self, textvariable=self.supplier_no_before,bg=self.color).grid(row=7, column=self.column+2, padx=5)
        self.row = 8
        Label(self, text='更新为：').grid(row=self.row, column=0)
        Label(self, text='供应商号：').grid(row=self.row, column=1)
        Entry(self, textvariable=self.supplier_no).grid(row=self.row, column=2, padx=5)
        # self.supplier_no.set('001')
        Label(self, text='供应商名: ').grid(row=self.row, column=3)
        Entry(self, textvariable=self.supplier_name).grid(row=self.row, column=4, padx=5)
        # self.supplier_name.set('天一')
        Label(self, text='所在城市: ').grid(row=self.row, column=5)
        Entry(self, textvariable=self.supplier_city).grid(row=self.row, column=6, padx=5)
        # self.supplier_city.set('西安')
        Button(self, text='更新', command=self.command_update_supplier).grid(row=self.row, column=8, padx=5)

        Label(self, text='更新客户信息').grid(row=9, column=0)
        Label(self, text='更新前客户号：',bg=self.color).grid(row=9, column=self.column)
        Entry(self, textvariable=self.customer_no_before,bg=self.color).grid(row=9, column=self.column+2, padx=5)
        self.row = 10
        Label(self, text='更新为：').grid(row=self.row, column=0)
        Label(self, text='客户号：').grid(row=self.row, column=1)
        Entry(self, textvariable=self.customer_no).grid(row=self.row, column=2, padx=5)
        # self.customer_no.set('001')
        Label(self, text='客户名: ').grid(row=self.row, column=3)
        Entry(self, textvariable=self.customer_name).grid(row=self.row, column=4, padx=5)
        # self.customer_name.set('李客户')
        Label(self, text='客户城市: ').grid(row=self.row, column=5)
        Entry(self, textvariable=self.customer_city).grid(row=self.row, column=6, padx=5)
        # self.customer_city.set('西安')
        Button(self, text='更新', command=self.command_update_customer).grid(row=self.row, column=8, padx=5)

        Label(self, text='更新库房信息').grid(row=11, column=0)
        Label(self, text='更新前库房号：',bg=self.color).grid(row=11, column=self.column)
        Entry(self, textvariable=self.warehouse_no_before,bg=self.color).grid(row=11, column=self.column+2, padx=5)
        self.row = 12
        Label(self, text='更新为：').grid(row=self.row, column=0)
        Label(self, text='库房号：').grid(row=self.row, column=1)
        Entry(self, textvariable=self.warehouse_no).grid(row=self.row, column=2, padx=5)
        # self.warehouse_no.set('001')
        Label(self, text='库房名: ').grid(row=self.row, column=3)
        Entry(self, textvariable=self.warehouse_name).grid(row=self.row, column=4, padx=5)
        # self.warehouse_name.set('李客户')
        Label(self, text='管理人工号: ').grid(row=self.row, column=5)
        Entry(self, textvariable=self.warehouse_employee_no).grid(row=self.row, column=6, padx=5)
        # self.warehouse_employee_no.set('20220001')
        self.row = 13
        Label(self, text='存储总量: ').grid(row=self.row, column=1)
        Entry(self, textvariable=self.warehouse_sum).grid(row=self.row, column=2, padx=5)
        # self.warehouse_sum.set('34')
        Button(self, text='更新', command=self.command_update_warehouse).grid(row=self.row, column=8, padx=5)

    def command_update_drug(self):
        if update_drug(self.drug_no_before.get(),self.drug_no.get(),
                       self.drug_name.get(), self.drug_level.get(),
                       self.drug_price.get()):
            showinfo(title='提示', message='更新数据成功！')
        else:
            showinfo(title='错误', message='更新数据失败！')

    def command_update_employee(self):
        if update_employee(self.employee_no_before.get(),self.employee_no.get(), self.employee_name.get(),
                           self.employee_age.get(), self.employee_sex.get(),
                           self.employee_date.get()):
            showinfo(title='提示', message='更新数据成功！')
        else:
            showinfo(title='错误', message='更新数据失败！')

    def command_update_supplier(self):
        if update_supplier(self.supplier_no_before.get(),self.supplier_no.get(),
                           self.supplier_name.get(), self.supplier_city.get()):
            showinfo(title='提示', message='更新数据成功！')
        else:
            showinfo(title='错误', message='更新数据失败！')

    def command_update_customer(self):
        if update_customer(self.customer_no_before.get(), self.customer_no.get(),self.customer_name.get(), self.customer_city.get()):
            showinfo(title='提示', message='更新数据成功！')
        else:
            showinfo(title='错误', message='更新数据失败！')

    def command_update_warehouse(self):
        if update_warehouse(self.warehouse_no_before.get(), self.warehouse_no.get(),
                            self.warehouse_name.get(),
                            self.warehouse_employee_no.get(), self.warehouse_sum.get()):
            showinfo(title='提示', message='更新数据成功！')
        else:
            showinfo(title='错误', message='更新数据失败！')

