#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/21 23:41
# @Author  : SZQ
from flask import *

from dbUtils import DbUtils

bpBooks = Blueprint(name="Books", import_name=__name__)

dbUtils = DbUtils()


@bpBooks.route("/")
def index():
    return render_template("index.html")


@bpBooks.route("/list", methods=["GET"])
def list():
    data = dbUtils.select()
    return data


@bpBooks.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    elif request.method == "POST":
        name = request.values.get("name")
        price = request.values.get("price")
        summary = request.values.get("summary")
        quantity = request.values.get("quantity")
        data = dbUtils.add(name, price, summary, quantity)
        return data
    else:
        return {"code": 0, "result": "illegal"}


# 下面暂未完成
@bpBooks.route("/delete", methods=["POST"])
def delete():
    if request.method == "POST":
        bid = request.values.get("bid")
        data = dbUtils.delete(bid)
        return data
    else:
        return {"code": 0, "result": "illegal"}


@bpBooks.route("/update", methods=["GET", "POST"])
def update():
    if request.method == "GET":
        return render_template("update.html")
    elif request.method == "POST":
        bid = request.values.get("bid")
        name = request.values.get("name")
        price = request.values.get("price")
        summary = request.values.get("summary")
        quantity = request.values.get("quantity")
        data = dbUtils.update(bid, name, price, summary, quantity)
        return data
    else:
        return {"code": 0, "result": "illegal"}


@bpBooks.route("/search", methods=["GET"])
def search():
    if request.method == "GET":
        info = request.values.get("info")
        data = dbUtils.select(info)
        return data
    else:
        return {"code": 0, "result": "illegal"}
