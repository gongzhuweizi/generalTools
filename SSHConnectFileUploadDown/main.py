#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：generalTools
@File ：main.py
@Author ：zhangyi
@Date ：2022/1/13 2:19 PM
'''
import sys
import ansible.inventory.data
from SSHConnectFileUploadDown import SSHConnectFileUploadDown
if __name__ == '__main__':
	s = SSHConnectFileUploadDown(
		hostname='8.210.8.255',
		port=22,
		username='root'
)
	s.set_private_key_file("/Users/zhangyi/.ssh/id_rsa")
	# s.set_exec_command('lssss')
	# result = s.get_exec_remote_command_result()
	# stdout = result.stderr.readlines()
	# print(stdout)
	# s.set_ssh_password("jj89757***")
	s.set_des_file_dir('/root/anna.py')
	s.set_src_file_dir('/Users/zhangyi/Desktop/anna.py')
	result = s.put_file_result()
	result1 = s.get_file_result()
	print(result,result1)






