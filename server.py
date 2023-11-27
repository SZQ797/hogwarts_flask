#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/21 21:39
# @Author  : SZQ
"""
建库建表语句

CREATE DATABASE bms;

CREATE TABLE book (
    bid INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    price FLOAT DEFAULT(0),
    summary VARCHAR(255),
    quantity INT DEFAULT(0)
);

"""
from flask_cors import CORS

from bookControl import *

app = Flask(__name__)
"""解决跨域问题"""
CORS(app)

# 感谢 北京-5-Gemini 大哥提供的解决方法，解决了F12的preview里中文正常，response里中文乱码的问题🫡
app.json.ensure_ascii = False

app.register_blueprint(bpBooks)

app.run(debug=True)

