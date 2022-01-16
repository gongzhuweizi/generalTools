#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：generalTools
@File ：test.py
@Author ：zhangyi
@Date ：2022/1/5 3:16 PM
'''
lis = [x for x in range(10)]
print(lis)
generator_ex = (x for x in range(10))
print(generator_ex.__next__())
