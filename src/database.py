import pymysql
import tkinter as tk
from tkinter import *
from tkinter.messagebox import *
from LoginPage import *
import datetime
db=None

now=datetime.datetime.now()
now_date=now.strftime("%Y/%m/%d")

def name_password(name,password):
    global db
    try:
        db=pymysql.connect(host='localhost',
                                     user=name,
                                     password=password,
                                     database='drug_manage')
    except:
        return False
    return True

#添加数据*********************************************************************************
def insert_drug(drug_no,drug_name,drug_level,drug_price):
    try:
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql="insert into drug_manage.drug values('%s','%s','%s','%s')"%(drug_no,drug_name,drug_level,drug_price)
        # 使用 execute()  方法执行 SQL，获取数据库版本
        cursor.execute(sql)
        cursor.close()
        # 关闭游标
        db.commit()#必须提交事务，不然不会更新数据库。
    except:
        return False
    else:
        return True
def insert_employee(employee_no,employee_name,employee_age,employee_sex,employee_date):
    try:
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql="insert into drug_manage.employee values('%s','%s','%s','%s','%s')"%(
            employee_no, employee_name,(str)(employee_age), employee_sex,employee_date)
        cursor.execute(sql)
        cursor.close()
        db.commit()#必须提交事务，不然不会更新数据库。
    except:
        return False
    else:
        return True
def insert_supplier(supplier_no,supplier_name,supplier_city):
    try:
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql = "insert into drug_manage.supplier values('%s','%s','%s')" % (
            supplier_no, supplier_name, supplier_city)
        cursor.execute(sql)
        cursor.close()
        db.commit()  # 必须提交事务，不然不会更新数据库。
    except:
        return False
    else:
        return True
def insert_customer(customer_no,customer_name,customer_city):
    try:
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql = "insert into drug_manage.customer values('%s','%s','%s')" % (
            customer_no, customer_name, customer_city)
        cursor.execute(sql)
        cursor.close()
        db.commit()  # 必须提交事务，不然不会更新数据库。
    except:
        return False
    else:
        return True
def insert_warehouse(warehouse_no,warehouse_name,warehouse_employee_no):
    try:
        warehouse_sum=0
        #查询总量
        cursor = db.cursor()
        sql="select sum(store_relation.store_num) from store_relation where warehouse_no='%s';"%(
            warehouse_no)
        cursor.execute(sql)
        data = cursor.fetchone()
        cursor.close()
        db.commit()
        cursor = db.cursor()
        sql = "insert into drug_manage.warehouse values('%s','%s','%s','%s')" % (
            warehouse_no, warehouse_name, warehouse_employee_no,str(data[0]))
        cursor.execute(sql)
        cursor.close()
        db.commit()  # 必须提交事务，不然不会更新数据库。
    except:
        return False
    else:
        return True

#删除数据*********************************************************************************
def delete_drug(drug_no,drug_name,drug_level,drug_price):
    try:
        sql = "select drug_no from drug where "
        len_origin = len(sql)
        if drug_no != '':
            sql = sql + " drug_no='%s' and" % (drug_no)
        if drug_name != '':
            sql = sql + " drug_name='%s' and" % (drug_name)
        if drug_level != '':
            sql = sql + " drug_level='%s' and" % (drug_level)
        if drug_price != '':
            sql = sql + " drug_price='%s' and" % (drug_price)
        if len_origin == len(sql):  # 证明全部为空
            sql = "select drug_no from drug "
        else:
            sql=sql[0:-3]
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        # data:(('0001',), ('0004',), ('0005',), ('001',), ('002',), ('003',))
        if len(data)==0:
            showinfo(title='提示', message='数据不存在！')
            return False
        for i in range(0,len(data)):
            sql="delete from drug where drug_no='%s' " % (data[i][0])
            cursor.execute(sql)
        cursor.close()
        db.commit()
    except:
        return False
    else:
        return True
def delete_employee(employee_no,employee_name,employee_age,employee_sex,employee_date):
    try:
        sql = "select employee_no from employee where "
        len_origin = len(sql)
        if employee_no != '':
            sql = sql + " employee_no='%s' and" % (employee_no)
        if employee_name != '':
            sql = sql + " employee_name='%s' and" % (employee_name)
        if employee_age != '':
            sql = sql + " employee_age='%s' and" % (employee_age)
        if employee_sex != '':
            sql = sql + " employee_sex='%s' and" % (employee_sex)
        if employee_date != '':
            sql = sql + " employee_date='%s' and" % (employee_date)
        if len_origin == len(sql):  # 证明全部为空
            sql = "select employee_no from employee "
        else:
            sql=sql[0:-3]
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        if len(data)==0:
            showinfo(title='提示', message='数据不存在！')
            return False
        for i in range(0,len(data)):
            sql="delete from employee where employee_no='%s' " % (data[i][0])
            cursor.execute(sql)
        cursor.close()
        db.commit()
    except:
        return False
    else:
        return True
def delete_supplier(supplier_no,supplier_name,supplier_city):
    try:
        sql = "select * from supplier where "
        len_origin = len(sql)
        if supplier_no != '':
            sql = sql + " supplier_no='%s' and" % (supplier_no)
        if supplier_name != '':
            sql = sql + " supplier_name='%s' and" % (supplier_name)
        if supplier_city != '':
            sql = sql + " supplier_city='%s' and" % (supplier_city)
        if len_origin == len(sql):  # 证明全部为空
            sql = "select * from supplier "
        else:
            sql=sql[0:-3]
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        if len(data)==0:
            showinfo(title='提示', message='数据不存在！')
            return False
        for i in range(0,len(data)):
            sql="delete from supplier where supplier_no='%s' " % (data[i][0])
            cursor.execute(sql)
        cursor.close()
        db.commit()
    except:
        return False
    else:
        return True
def delete_customer(customer_no,customer_name,customer_city):
    try:
        sql = "select * from customer where "
        len_origin = len(sql)
        if customer_no != '':
            sql = sql + " customer_no='%s' and" % (customer_no)
        if customer_name != '':
            sql = sql + " customer_name='%s' and" % (customer_name)
        if customer_city != '':
            sql = sql + " customer_city='%s' and" % (customer_city)
        if len_origin == len(sql):  # 证明全部为空
            sql = "select * from customer "
        else:
            sql=sql[0:-3]
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        if len(data)==0:
            showinfo(title='提示', message='数据不存在！')
            return False
        for i in range(0,len(data)):
            sql="delete from customer where customer_no='%s' " % (data[i][0])
            cursor.execute(sql)
        cursor.close()
        db.commit()
    except:
        return False
    else:
        return True
def delete_warehouse(warehouse_no,warehouse_name,warehouse_employee_no,warehouse_sum):
    try:
        sql="select * from warehouse where "
        len_origin=len(sql)
        if warehouse_no!='':
            sql=sql+" warehouse_no='%s' and"%(warehouse_no)
        if warehouse_name!='':
            sql=sql+" warehouse_name='%s' and"%(warehouse_name)
        if warehouse_employee_no!='':
            sql=sql+" warehouse_employee_no='%s' and"%(warehouse_employee_no)
        if warehouse_sum!='':
            sql=sql+" warehouse_sum='%s' and"%(warehouse_sum)
        if len_origin==len(sql):#证明全部为空
            sql = "select * from warehouse "
        else:
            sql=sql[0:-3]
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        if len(data)==0:
            showinfo(title='提示', message='数据不存在！')
            return False
        for i in range(0,len(data)):
            sql="delete from warehouse where warehouse_no='%s' " % (data[i][0])
            cursor.execute(sql)
        cursor.close()
        db.commit()

    except:
        return False
    else:
        return True

#更新数据*********************************************************************************
def update_drug(drug_no_before,drug_no,drug_name,drug_level,drug_price):
    try:
        sql="select * from drug where drug_no='%s' "%(drug_no_before)
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        if len(data) == 0:#没有可以更新的数据
            showinfo(title='提示', message='数据不存在！')
            return False
        sql = "update drug set "
        len_origin = len(sql)
        if drug_no != '':
            sql = sql + " drug_no='%s' ," % (drug_no)
        if drug_name != '':
            sql = sql + " drug_name='%s' ," % (drug_name)
        if drug_level != '':
            sql = sql + " drug_level='%s' ," % (drug_level)
        if drug_price != '':
            sql = sql + " drug_price='%s' ," % (drug_price)
        if len_origin == len(sql):  # 证明全部为空
            return False
        else:
            sql = sql[0:-1]+"where drug_no='%s' "%(drug_no_before)
        cursor.execute(sql)
        cursor.close()
        db.commit()
    except:
        return False
    else:
        return True
def update_employee(employee_no_before,employee_no,employee_name,employee_age,employee_sex,employee_date):
    try:
        sql = "select * from employee where employee_no='%s' " % (employee_no_before)
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        if len(data) == 0:  # 没有可以更新的数据
            showinfo(title='提示', message='数据不存在！')
            return False
        sql = "update employee set "
        len_origin = len(sql)
        if employee_no != '':
            sql = sql + " employee_no='%s' ," % (employee_no)
        if employee_name != '':
            sql = sql + " employee_name='%s' ," % (employee_name)
        if employee_age != '':
            sql = sql + " employee_age='%s' ," % (employee_age)
        if employee_sex != '':
            sql = sql + " employee_sex='%s' ," % (employee_sex)
        if employee_date != '':
            sql = sql + " employee_date='%s' ," % (employee_date)
        if len_origin == len(sql):  # 证明全部为空
            return False
        else:
            sql = sql[0:-1]+"where employee_no='%s' "%(employee_no_before)
        cursor.execute(sql)
        cursor.close()
        db.commit()
    except:
        return False
    else:
        return True
def update_supplier(supplier_no_before,supplier_no,supplier_name,supplier_city):
    try:
        sql = "select * from supplier where supplier_no='%s' " % (supplier_no_before)
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        if len(data) == 0:  # 没有可以更新的数据
            showinfo(title='提示', message='数据不存在！')
            return False
        sql = "update supplier set "
        len_origin = len(sql)
        if supplier_no != '':
            sql = sql + " supplier_no='%s' ," % (supplier_no)
        if supplier_name != '':
            sql = sql + " supplier_name='%s' ," % (supplier_name)
        if supplier_city != '':
            sql = sql + " supplier_city='%s' ," % (supplier_city)
        if len_origin == len(sql):  # 证明全部为空
            return False
        else:
            sql = sql[0:-1]+"where supplier_no='%s' "%(supplier_no_before)
        cursor = db.cursor()
        cursor.execute(sql)
        cursor.close()
        db.commit()
    except:
        return False
    else:
        return True
def update_customer(customer_no_before,customer_no,customer_name,customer_city):
    try:
        sql = "select * from customer where customer_no='%s' " % (customer_no_before)
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        if len(data) == 0:  # 没有可以更新的数据
            showinfo(title='提示', message='数据不存在！')
            return False
        sql = "update customer set "
        len_origin = len(sql)
        if customer_no != '':
            sql = sql + " customer_no='%s' ," % (customer_no)
        if customer_name != '':
            sql = sql + " customer_name='%s' ," % (customer_name)
        if customer_city != '':
            sql = sql + " customer_city='%s' ," % (customer_city)
        if len_origin == len(sql):  # 证明全部为空
            return False
        else:
            sql = sql[0:-1]+" where customer_no='%s' "%(customer_no_before)
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        db.commit()
    except:
        return False
    else:
        return True
def update_warehouse(warehouse_no_before,warehouse_no,warehouse_name,warehouse_employee_no,warehouse_sum):
    try:
        sql = "select * from warehouse where warehouse_no='%s' " % (warehouse_no_before)
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        if len(data) == 0:  # 没有可以更新的数据
            showinfo(title='提示', message='数据不存在！')
            return False
        sql = "update warehouse set "
        len_origin=len(sql)
        if warehouse_no!='':
            sql=sql+" warehouse_no='%s' ,"%(warehouse_no)
        if warehouse_name!='':
            sql=sql+" warehouse_name='%s' ,"%(warehouse_name)
        if warehouse_employee_no!='':
            sql=sql+" warehouse_employee_no='%s' ,"%(warehouse_employee_no)
        if warehouse_sum!='':
            sql=sql+" warehouse_sum='%s' ,"%(warehouse_sum)
        if len_origin == len(sql):  # 证明全部为空
            return False
        else:
            sql = sql[0:-1]+" where warehouse_no='%s' "%(warehouse_no_before)
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        db.commit()

    except:
        return False
    else:
        return True

#查询数据*********************************************************************************
def select_drug(drug_no,drug_name,drug_level,drug_price):
    list_attribute = ['drug_no', '\tdrug_name', '\tdrug_level','\tdrug_price']
    try:
        sql = "select * from drug where "
        len_origin = len(sql)
        if drug_no != '':
            sql = sql + " drug_no='%s'  and" % (drug_no)
        if drug_name != '':
            sql = sql + " drug_name='%s' and" % (drug_name)
        if drug_level != '':
            sql = sql + " drug_level='%s' and" % (drug_level)
        if drug_price !='':
            sql = sql + " drug_price='%s' and" % (drug_price)
        if len_origin == len(sql):  # 证明全部为空
            sql = "select * from drug "
        else:
            sql=sql[0:-3]
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        # 调用函数展示
        show_select(list_attribute, data)
        cursor.close()
        db.commit()
    except:
        return False
    else:
        return True
def select_employee(employee_no,employee_name,employee_age,employee_sex,employee_date):
    list_attribute = ['employee_no', '\temployee_name', '\temployee_age',
                      '\temployee_sex', '\temployee_date']
    try:
        sql = "select * from employee where "
        len_origin = len(sql)
        if employee_no != '':
            sql = sql + " employee_no='%s'  and" % (employee_no)
        if employee_name != '':
            sql = sql + " employee_name='%s'  and" % (employee_name)
        if employee_age != '':
            sql = sql + " employee_age='%s'  and" % (employee_age)
        if employee_sex != '':
            sql = sql + " employee_sex='%s'  and" % (employee_sex)
        if employee_date != '':
            sql = sql + " employee_date='%s'  and" % (employee_date)
        if len_origin == len(sql):  # 证明全部为空
            sql = "select * from employee "
        else:
            sql=sql[0:-3]
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        # 调用函数展示
        show_select(list_attribute, data,580)
        cursor.close()
        db.commit()
    except:
        return False
    else:
        return True
def select_supplier(supplier_no,supplier_name,supplier_city):
    list_attribute = ['supplier_no', '\tsupplier_name', '\tsupplier_city']
    try:
        sql = "select * from supplier where "
        len_origin = len(sql)
        if supplier_no != '':
            sql = sql + " supplier_no='%s' and" % (supplier_no)
        if supplier_name != '':
            sql = sql + " supplier_name='%s' and" % (supplier_name)
        if supplier_city != '':
            sql = sql + " supplier_city='%s' and" % (supplier_city)
        if len_origin == len(sql):  # 证明全部为空
            sql = "select * from supplier "
        else:
            sql=sql[0:-3]
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        # 调用函数展示
        show_select(list_attribute, data,350)
        cursor.close()
        db.commit()
    except:
        return False
    else:
        return True
def select_customer(customer_no,customer_name,customer_city):
    list_attribute = ['customer_no', '\tcustomer_name', '\tcustomer_city']
    try:
        sql = "select * from customer where "
        len_origin = len(sql)
        if customer_no != '':
            sql = sql + " customer_no='%s' and" % (customer_no)
        if customer_name != '':
            sql = sql + " customer_name='%s' and" % (customer_name)
        if customer_city != '':
            sql = sql + " customer_city='%s' and" % (customer_city)
        if len_origin == len(sql):  # 证明全部为空
            sql = "select * from customer "
        else:
            sql=sql[0:-3]
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        # 调用函数展示
        show_select(list_attribute, data,350)
        cursor.close()
        db.commit()
    except:
        return False
    else:
        return True
def select_warehouse(warehouse_no,warehouse_name,warehouse_employee_no,warehouse_sum):
    list_attribute=['warehouse_no','\twarehouse_name','\tw_employee_no','warehouse_sum']
    try:
        sql="select * from warehouse where "
        len_origin=len(sql)
        if warehouse_no!='':
            sql=sql+" warehouse_no='%s' and"%(warehouse_no)
        if warehouse_name!='':
            sql=sql+" warehouse_name='%s' and"%(warehouse_name)
        if warehouse_employee_no!='':
            sql=sql+" warehouse_employee_no='%s' and"%(warehouse_employee_no)
        if warehouse_sum!='':
            sql=sql+" warehouse_sum='%s' and"%(warehouse_sum)
        if len_origin==len(sql):#证明全部为空
            sql = "select * from warehouse "
        else:
            sql=sql[0:-3]
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        #调用函数展示
        show_select(list_attribute, data)
        cursor.close()
        db.commit()

    except:
        return False
    else:
        return True
def select_sr():
    list_attribute=['supply_no','\tdrug_no','\twarehouse_no','\tsupplier_no','\tsupply_num','\tsupply_date']
    try:
        sql="select * from supply_relation "
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        #调用函数展示
        show_select(list_attribute, data,680)
        cursor.close()
        db.commit()
    except:
        return False
    else:
        return True
def select_store_r():
    list_attribute=['drug_no','\twarehouse_no','\tstore_num']
    try:
        sql="select * from store_relation "
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        #调用函数展示
        show_select(list_attribute, data,350)
        cursor.close()
        db.commit()
    except:
        return False
    else:
        return True
def select_sell():
    list_attribute=['sell_no','\temployee_no','\tdrug_no','\tcustomer_no','\twarehouse_no','\tsell_date','\tsell_num','\tcancel']
    try:
        sql="select * from sell "
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        #调用函数展示
        show_select(list_attribute, data,920)
        cursor.close()
        db.commit()
    except:
        return False
    else:
        return True
def show_select(list_attribute,list_data,width=460):
    root_select = Tk()
    root_select.title("查询")
    root_select.geometry("%dx300+10+10"%(width))
    stri=''
    for j in range(0, len(list_attribute)):
        stri = stri + list_attribute[j] + '\t'
    str=stri+'\n'
    for i in range(0, len(list_data)):
        stri = ''
        for j in range(0, len(list_attribute)):
            stri = stri + list_data[i][j] + '\t\t'
        stri=stri+'\n'
        str = str+stri
    text = tk.Text(root_select, width=256, height=15)
    text.pack(side=tk.LEFT, fill=tk.Y)
    text.insert(tk.INSERT, str)

#供应关系*********************************************************************************
def supply_relation(sr_supply_no,sr_drug_no,sr_warehouse_no,sr_supplier_no,sr_supply_num,sr_supply_date):
    try:
        cursor = db.cursor()
        sql="insert into supply_relation values('%s','%s','%s','%s','%s','%s');"%(
            sr_supply_no,sr_drug_no, sr_warehouse_no, sr_supplier_no, sr_supply_num, sr_supply_date)
        cursor.execute(sql)
        #存储关系需要添加数据
        store_num = int(sr_supply_num)
        sql = "select store_num from store_relation where drug_no='%s' and warehouse_no='%s' " % (
            sr_drug_no,sr_warehouse_no)
        cursor.execute(sql)
        data = cursor.fetchall()
        if len(data) == 0 :  # 不存在此存储关系
            sql="insert into store_relation values('%s','%s','%s')"%(
                sr_drug_no, sr_warehouse_no,str(store_num)
            )
            cursor.execute(sql)
            db.commit()
        elif data[0][0] == 'None' or data[0][0] == '0':
            pass
        else:
            store_num += int(data[0][0])
        sql = "update store_relation set store_num='%s' where drug_no='%s' and warehouse_no='%s' " % (
             str(store_num),sr_drug_no, sr_warehouse_no)
        cursor.execute(sql)

        # 仓库的数目要增加
        #先统计存储关系该仓库的存储量
        warehouse_sum = 0
        sql = "select store_num from store_relation where warehouse_no='%s' ;" % (sr_warehouse_no)
        cursor.execute(sql)
        data = cursor.fetchall()
        for i in range(0,len(data)):
            warehouse_sum += int(data[i][0])
        sql = "update warehouse set warehouse_sum='%s' where warehouse_no='%s' ;" % (
            str(warehouse_sum), sr_warehouse_no)
        cursor.execute(sql)

        cursor.close()
        db.commit()#必须提交事务，不然不会更新数据库。
    except:
        return False
    else:
        return True
#销售************************************************************************************
def sell(sell_sell_no,sell_employee_no,sell_drug_no,sell_customer_no,sell_warehouse_no,sell_sell_date,sell_sell_num,sell_cancel):
    try:
        # 判断存储关系的库存数是否够
        cursor = db.cursor()
        sql = "select store_num from store_relation where drug_no='%s' and warehouse_no='%s' " % (
            sell_drug_no,sell_warehouse_no)
        cursor.execute(sql)
        data = cursor.fetchall()
        store_num = int(data[0][0])
        if int(data[0][0])>=int(sell_sell_num):
            #卖出,库存数目减少
            store_num-=int(sell_sell_num)
            sql = "update store_relation set store_num='%s' where drug_no='%s' and warehouse_no='%s' " % (
                str(store_num), sell_drug_no, sell_warehouse_no)
            print(sql)
            cursor.execute(sql)
        else:
            showinfo(title='提示', message='库存不足！')
            return False
        # 仓库的数目要减少
        #先统计存储关系该仓库的存储量
        warehouse_sum = 0
        sql = "select store_num from store_relation where warehouse_no='%s' ;" % (sell_warehouse_no)
        cursor.execute(sql)
        data = cursor.fetchall()
        for i in range(0,len(data)):
            warehouse_sum += int(data[i][0])
        sql = "update warehouse set warehouse_sum='%s' where warehouse_no='%s' ;" % (
            str(warehouse_sum), sell_warehouse_no)
        cursor.execute(sql)
        #销售
        sql="insert into sell values('%s','%s','%s','%s','%s','%s','%s','%s');"%(
            sell_sell_no, sell_employee_no, sell_drug_no,
            sell_customer_no,sell_warehouse_no, sell_sell_date,
            sell_sell_num, sell_cancel)
        cursor.execute(sql)
        cursor.close()
        db.commit()#必须提交事务，不然不会更新数据库。
    except:
        return False
    else:
        return True

#统计************************************************************************************
def statistics_day(statistics_day):
    list_attribute = ['statistics_date', '\t\tsell_sum_price']

    try:
        sum_price=0
        cursor = db.cursor()
        sql="select drug_no,sell_num,cancel from sell where sell_date='%s' "%(statistics_day)
        cursor.execute(sql)
        data = cursor.fetchall()
        for i in range(0,len(data)):
            if data[i][2]=='是':
                continue
            sql="select drug_price from drug where drug_no='%s' "%(data[i][0])
            cursor.execute(sql)
            data_price = cursor.fetchall()
            sum_price=int(data_price[0][0])*int(data[i][1])
        #展示统计的数目
        list_data=[[statistics_day,'\t'+str(sum_price)],]
        show_select(list_attribute, list_data)
        cursor.close()
        db.commit()
    except:
        return False
    else:
        return True
def statistics_month(statistics_month):
    list_attribute = ['statistics_month', '\t\tsell_sum_price']
    try:
        sum_price=0
        cursor = db.cursor()
        sql="select drug_no,sell_num,cancel from sell where sell_date regexp('^%s') "%(statistics_month)
        print(sql)
        cursor.execute(sql)
        data = cursor.fetchall()
        print(data)
        for i in range(0,len(data)):
            if data[i][2]=='是':
                continue
            sql="select drug_price from drug where drug_no='%s' "%(data[i][0])
            print(sql)
            cursor.execute(sql)
            data_price = cursor.fetchall()
            sum_price=int(data_price[0][0])*int(data[i][1])
        #展示统计的数目
        list_data=[[statistics_month,'\t'+str(sum_price)],]
        show_select(list_attribute, list_data)
        cursor.close()
        db.commit()
    except:
        return False
    else:
        return True
#退货处理********************************************************************************
def cancel_sell(cancel_sell_no):
    try:
        cursor = db.cursor()
        sql="select cancel from sell where sell_no='%s' "%(cancel_sell_no)
        cursor.execute(sql)
        data=cursor.fetchall()
        if data[0][0]=='是':#已经退过了
            showinfo(title='提示', message='已经退过！')
            return False
        sql="select drug_no,warehouse_no from sell where sell_no='%s' "%(cancel_sell_no)
        cursor.execute(sql)
        data2=cursor.fetchall()
        #计算存储关系的存储量
        sql = "select store_num from store_relation where drug_no='%s' and warehouse_no='%s' " % (
            data2[0][0], data2[0][1])
        cursor.execute(sql)
        data = cursor.fetchall()
        store_num = int(data[0][0])
        print(store_num)
        sql="select sell_num from sell where sell_no='%s' "%(cancel_sell_no)
        cursor.execute(sql)
        data = cursor.fetchall()
        store_num=int(data[0][0])+store_num#退货
        #存储关系库存增加
        sql= "update store_relation set store_num='%s' where drug_no='%s' and warehouse_no='%s' " % (
                str(store_num),data2[0][0], data2[0][1])
        cursor.execute(sql)
        #仓库库存重新计算
        # 先统计存储关系该仓库的存储量
        warehouse_sum = 0
        sql = "select store_num from store_relation where warehouse_no='%s' ;" % ( data2[0][1])
        cursor.execute(sql)
        data = cursor.fetchall()
        for i in range(0, len(data)):
            warehouse_sum += int(data[i][0])
        sql = "update warehouse set warehouse_sum='%s' where warehouse_no='%s' ;" % (
            str(warehouse_sum),  data2[0][1])
        cursor.execute(sql)
        sql = " update sell set cancel='是' where sell_no='%s' "%(cancel_sell_no)
        cursor.execute(sql)
        cursor.close()
        db.commit()#必须提交事务，不然不会更新数据库。
    except:
        return False
    else:
        return True