#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：generalTools
@File ：CompressionImages1.py.py
@Author ：zhangyi
@Date ：2022/3/24 1:44 PM
'''
import configparser

"""
把压缩结果写入文件，用于记录
"""
def write_log_file(logFile,content):
	with open(logFile,'a+') as f:
		f.write(content+'\n')

"""
主函数
"""
if '__name__' == '__main__':
	compressionTotalCount = 0
	compressionSuccessCount = 0
	compressionFailCount = 0
	config = configparser.ConfigParser()
	config.read('config.ini', encoding='utf-8')
	pngCompressionCommand = config.get('pngquant', 'bin_command')





