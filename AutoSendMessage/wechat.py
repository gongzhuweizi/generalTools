#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：generalTools 
@File ：wechat.py
@Author ：zhangyi
@Date ：2022/8/5 5:15 PM 
'''
import itchat

itchat.auto_login()

itchat.send('Hello, filehelper', toUserName='filehelper')
