from tkinter import *
from tkinter.messagebox import *
from LoginPage import *
from database import *

class ServerFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.row=0#定义类变量
        self.column=0
        self.root = master  # 定义内部变量root
        self.sr_supply_no=StringVar()
        self.sr_drug_no = StringVar()
        self.sr_warehouse_no = StringVar()
        self.sr_supplier_no = StringVar()
        self.sr_supply_num = StringVar()
        self.sr_supply_date = StringVar()

        self.sell_sell_no=StringVar()
        self.sell_employee_no = StringVar()
        self.sell_drug_no = StringVar()
        self.sell_customer_no = StringVar()
        self.sell_warehouse_no = StringVar()
        self.sell_sell_date = StringVar()
        self.sell_sell_num = StringVar()
        self.sell_cancel = StringVar()

        self.statistics_day=StringVar()
        self.statistics_month=StringVar()

        self.cancel_sell_no=StringVar()
        self.createPage()

    def createPage(self):
        Label(self, text='供应药品').grid(row=1, column=0)
        self.row=2
        Label(self, text='供应单号：').grid(row=self.row, column=1)
        Entry(self, textvariable=self.sr_supply_no).grid(row=self.row, column=2, padx=5)
        self.sr_supply_no.set('0001')
        Label(self, text='药品号：').grid(row=self.row, column=3)
        Entry(self, textvariable=self.sr_drug_no).grid(row=self.row, column=4,padx=5)
        self.sr_drug_no.set('0001')
        Label(self, text='库房号: ').grid(row=self.row, column=5)
        Entry(self, textvariable=self.sr_warehouse_no).grid(row=self.row, column=6,padx=5)
        self.sr_warehouse_no.set('001')
        self.row = 3
        Label(self, text='供应商号: ').grid(row=self.row,column=1)
        Entry(self, textvariable=self.sr_supplier_no).grid(row=self.row, column=2,padx=5)
        self.sr_supplier_no.set('001')
        Label(self, text='进货量: ').grid(row=self.row, column=3)
        Entry(self, textvariable=self.sr_supply_num).grid(row=self.row, column=4, padx=5)
        self.sr_supply_num.set('300')
        Label(self, text='进货日期: ').grid(row=self.row, column=5)
        Entry(self, textvariable=self.sr_supply_date).grid(row=self.row, column=6, padx=5)
        self.sr_supply_date.set('' + str(now_date))  # 当前日期
        Button(self, text='供应', command=self.command_supply_relation).grid(row=self.row, column=8,padx=5)

        Label(self, text='销售').grid(row=4, column=0)
        self.row = 5
        Label(self, text='销售编号：').grid(row=self.row, column=1)
        Entry(self, textvariable=self.sell_sell_no).grid(row=self.row, column=2, padx=5)
        self.sell_sell_no.set('0001')
        Label(self, text='员工号：').grid(row=self.row, column=3)
        Entry(self, textvariable=self.sell_employee_no).grid(row=self.row, column=4, padx=5)
        self.sell_employee_no.set('20220001')
        Label(self, text='药品号: ').grid(row=self.row, column=5)
        Entry(self, textvariable=self.sell_drug_no).grid(row=self.row, column=6, padx=5)
        self.sell_drug_no.set('0001')
        self.row = 6
        Label(self, text='客户号: ').grid(row=self.row, column=1)
        Entry(self, textvariable=self.sell_customer_no).grid(row=self.row, column=2, padx=5)
        self.sell_customer_no.set('001')
        Label(self, text='出货仓库号: ').grid(row=self.row, column=3)
        Entry(self, textvariable=self.sell_warehouse_no).grid(row=self.row, column=4, padx=5)
        self.sell_warehouse_no.set('001')
        Label(self, text='销售日期: ').grid(row=self.row, column=5)
        Entry(self, textvariable=self.sell_sell_date).grid(row=self.row, column=6, padx=5)
        self.sell_sell_date.set(str(now_date))  # 当前日期
        self.row = 7
        Label(self, text='销售量: ').grid(row=self.row, column=1)
        Entry(self, textvariable=self.sell_sell_num).grid(row=self.row, column=2, padx=5)
        self.sell_sell_num.set('10')
        Button(self, text='销售', command=self.command_sell).grid(row=self.row, column=8, padx=5)

        Label(self, text='财务统计').grid(row=8, column=0)
        self.row = 9
        Label(self, text='当日统计：').grid(row=self.row, column=1)
        Entry(self, textvariable=self.statistics_day).grid(row=self.row, column=2, padx=5)
        self.statistics_day.set(str(now_date))
        Button(self, text='统计', command=self.command_statistics_day).grid(row=self.row, column=8, padx=5)
        self.row = 10
        Label(self, text='当月统计：').grid(row=self.row, column=1)
        Entry(self, textvariable=self.statistics_month).grid(row=self.row, column=2, padx=5)
        self.statistics_month.set(str(now_date)[0:-3])
        Button(self, text='统计', command=self.command_statistics_month).grid(row=self.row, column=8, padx=5)

        Label(self, text='退货').grid(row=11, column=0, ipady=10)
        self.row = 12
        Label(self, text='销售单号：').grid(row=self.row, column=1)
        Entry(self, textvariable=self.cancel_sell_no).grid(row=self.row, column=2, padx=5)
        self.cancel_sell_no.set('0001')
        Button(self, text='退货', command=self.command_cancel_sell).grid(row=self.row, column=8, padx=5)


    def command_supply_relation(self):
        if supply_relation(self.sr_supply_no.get(),
                self.sr_drug_no.get(),self.sr_warehouse_no.get(),
                           self.sr_supplier_no.get(),self.sr_supply_num.get(),
                           self.sr_supply_date.get()):
            showinfo(title='提示', message='成功供应！')
        else:
            showinfo(title='错误', message='供应失败！')
    def command_sell(self):
        self.sell_cancel='否'
        if sell(self.sell_sell_no.get(),self.sell_employee_no.get(),
                self.sell_drug_no.get(),self.sell_customer_no.get(),
                           self.sell_warehouse_no.get(),self.sell_sell_date.get(),
                           self.sell_sell_num.get(),self.sell_cancel):
            showinfo(title='提示', message='成功销售！')
        else:
            showinfo(title='错误', message='销售失败！')
    def command_statistics_day(self):
        if statistics_day(self.statistics_day.get()):
            pass
        else:
            showinfo(title='错误', message='统计失败！')
    def command_statistics_month(self):
        if statistics_month(self.statistics_month.get()):
            pass
        else:
            showinfo(title='错误', message='统计失败！')
    def command_cancel_sell(self):
        if cancel_sell(self.cancel_sell_no.get()):
            showinfo(title='提示', message='退货成功！')
        else:
            showinfo(title='错误', message='退货失败！')








