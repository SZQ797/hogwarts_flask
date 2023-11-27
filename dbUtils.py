#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/22 00:05
# @Author  : SZQ
from pymysql import *


class DbUtils:

    def __init__(self):
        self.db_connect = None

    def connect(self):
        self.db_connect = Connect(user="root", password="88888888", database="bms", charset="utf8mb4")

    def close_connection(self):
        self.db_connect.commit()
        self.db_connect.close()

    def select(self, info=None):
        self.connect()

        cursor = self.db_connect.cursor()
        sql = """SELECT * FROM book WHERE 1=1 """
        if info:
            sql += f"AND name LIKE '%{info}%' OR summary LIKE '%{info}%'"

        print(f"执行的SQL是：{sql}")
        cursor.execute(sql)
        data = cursor.fetchall()
        # print(f"查询结果：{data}")

        datas = []
        for i in data:
            book = {}
            book["bid"] = i[0]
            book["name"] = i[1]
            book["price"] = i[2]
            book["summary"] = i[3]
            book["quantity"] = i[4]

            datas.append(book)
        # print(f"datas是：{datas}")

        cursor.close()
        self.close_connection()
        return datas

    def add(self, name, price, summary, quantity):
        self.connect()
        cursor = self.db_connect.cursor()
        sql_select = f"""SELECT * FROM book WHERE name = '{name}'"""
        print(f"执行的SQL是:{sql_select}")
        # sql = ""
        cursor.execute(sql_select)
        data = cursor.fetchall()
        print(f"查询结果：{data}")

        if data:
            b_id = data[0][0]
            print(f"bid:{b_id}")
            b_quantity = int(data[0][4])
            print(f"b_quantity:{b_quantity}")
            print(type(b_quantity))
            b_quantity += int(quantity)
            # 更新数量
            sql = f"""UPDATE `book` SET `quantity` = {b_quantity} WHERE `bid` = {b_id}"""
        else:
            # 插入数据
            sql = f"""INSERT INTO book (`name`, `price`, `summary`, `quantity`) VALUES ('{name}', {price}, '{summary}', {quantity})"""

        print(f"执行的SQL是：{sql}")
        cursor.execute(sql)
        print(f"后来执行的SQL是:{sql}")

        cursor.close()
        self.close_connection()
        return {"code": 0, "result": "success"}

    def delete(self, bid):
        self.connect()
        cursor = self.db_connect.cursor()
        sql = f"""DELETE FROM book WHERE bid = '{bid}'"""
        print(f"执行的SQL是:{sql}")
        # sql = ""
        cursor.execute(sql)
        self.db_connect.commit()
        cursor.close()
        self.close_connection()
        return {"code": 0, "result": "success"}

    def update(self, bid, name, price, summary, quantity):
        self.connect()
        cursor = self.db_connect.cursor()
        sql = f"""UPDATE `book` SET `name` = '{name}', `price` = {price}, `summary` = '{summary}', `quantity` = {quantity} WHERE `bid` = {bid};"""

        print(f"执行的SQL是：{sql}")
        cursor.execute(sql)
        cursor.close()
        self.db_connect.commit()
        self.close_connection()
        return {"code": 0, "result": "success"}
