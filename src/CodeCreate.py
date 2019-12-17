#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
生成代码
'''
import os
import sys
import io
import time

basedir = os.path.abspath(os.path.dirname(__file__))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def creatOne(count: int):
    head = "else if (paramets.Length == %d)\n" \
           "    {\n        return Activator.CreateInstance(ctor.DeclaringType,\n" % count
    cur = "        "
    for index in range(0, count):
        if (index % 10 == 0 and index != 0):
            cur += "\n        "
        cur += "paramets[{}],".format(index)
    cur = cur[:-1]  # 去掉最后一个逗号
    end = ");}\n"
    item = head + cur + end
    print(item)
    return item


fh = open(basedir+"/code.cs", 'w')
for count in range(1, 100):
    item = creatOne(count)
    fh.write(item)
fh.close()
