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


@bpBooks.route("/add", methods=["POST"])
def add():
    name = request.values.get("name")
    price = request.values.get("price")
    summary = request.values.get("summary")
    quantity = request.values.get("quantity")
    data = dbUtils.add(name, price, summary, quantity)
    return data

# 下面暂未完成
@bpBooks.route("/delete", methods=["POST"])
def delete():
    return render_template("delete.html")


@bpBooks.route("/update", methods=["POST"])
def update():
    return render_template("update.html")


@bpBooks.route("/search", methods=["GET"])
def search():
    return render_template("search.html")
