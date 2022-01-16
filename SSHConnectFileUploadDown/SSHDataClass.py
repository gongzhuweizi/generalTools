#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：generalTools
@File ：SSHDataClass.py
@Author ：zhangyi
@Date ：2022/1/13 11:02 AM
'''
from dataclasses import dataclass
@dataclass
class ExecCommandDataClass:
	stdin : None
	stdout : None
	stderr : None

