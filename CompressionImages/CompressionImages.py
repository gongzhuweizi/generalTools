#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：generalTools
@File ：CompressionImages.py
@Author ：zhangyi
@Date ：2022/3/10 3:14 PM
'''
import os
import configparser
import subprocess
from PIL import Image
from colorama import Fore
import shutil


def judge_img(imgfile):
	if imgfile.endswith('jpg') or imgfile.endswith('JPG') or imgfile.endswith('png') or imgfile.endswith(
			'PNG') or imgfile.endswith('jpeg') or imgfile.endswith('JPEG') or imgfile.endswith(
		'svg') or imgfile.endswith('SVG'):
		return True

def exec_system_command(command):
	result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8",
							timeout=100)
	return result.returncode

def get_file_size(file):
	file_size = os.path.getsize(file)
	Byte = round(file_size, 2)
	KB = round(file_size / 1024, 2)
	MB = round(file_size / 1024 / 1024, 2)
	return {
		'Byte': Byte,
		'KB': KB,
		'MB': MB
	}

def compress_image(s_dir, d_dir, quality):
	try:
		im = Image.open(s_dir)
		im.save(d_dir, quality=quality)
		return True
	except Exception as e:
		return False
if __name__ == '__main__':
	s_file = open('s_file.txt', 'a+')
	f_file = open('f_file.txt', 'a+')
	all_file = open('all_file.txt', 'a+')
	s_count = 0
	f_count = 0
	all_count = 0
	copy_count = 0
	config = configparser.ConfigParser()
	config.read('config.ini', encoding='utf-8')
	default_png_command = config.get('pngquant', 'bin_command')
	png_quality = config.get('pngquant', 'quality')
	jpg_quality = int(config.get('jpg', 'quality'))
	img_src_dir = config.get('base', 'img_src_dir')
	img_des_dir = config.get('base', 'img_des_dir')
	default_svg_command = config.get('svg', 'bin_command')
	svg_config_file = config.get('svg', 'config_file')
	sort_list = []
	if os.path.isdir(img_src_dir):
		for root, dirs, files in os.walk(img_src_dir):
			fileLength = len(files)
			if fileLength != 0:
				all_count = all_count + fileLength
			for file in files:
				d_root = root.replace(img_src_dir, img_des_dir)
				s_dir = root + "/" + file
				d_dir = d_root + '/' + file
				all_file.write(s_dir + '\n')
				if file.startswith('.'):
					print(Fore.RED + "文件格式错误！.结尾的文件" + s_dir)
					f_count += 1
					f_file.write(s_dir + '\n')
					continue
				if judge_img(file) != True:
					print(Fore.RED + "文件格式不支持---源文件为:" + s_dir + "源文件直接复制！")
					shutil.copy(s_dir, d_dir)
					copy_count += 1
					f_file.write(s_dir + '\n')
					continue
				if not os.path.exists(d_root):
					try:
						os.mkdir(d_root)
					except Exception as e:
						print(Fore.RED + "创建文件失败，源文件为" + s_dir + str(e))
						exit(1)
				if file.endswith('.png') or file.endswith('.PNG'):
					png_command = default_png_command
					command_args = {'quality': png_quality, 'output': d_dir, 'command': png_command, 's_dir': s_dir}
					png_command = "{command} --quality={quality} --force --output={output} {s_dir} ".format(
						**command_args)
					if exec_system_command(png_command) == 0:
						src_file_size = get_file_size(s_dir)
						des_file_size = get_file_size(d_dir)
						perf = round(des_file_size['KB'] / src_file_size['KB'], 2)
						print(Fore.GREEN + '压缩成功!  源文件为:' + s_dir + ' 导出文件为:' + d_dir + "--->文件大小:" + str(
							des_file_size['KB']) + "KB" + "  压缩率为:" + str(perf))
						sort_list.append(des_file_size['KB'])
						s_file.write(s_dir + '\n')
						s_count += 1
					else:
						print(Fore.RED + "png图片转化失败，源文件路径为:" + s_dir + "源文件直接复制！")
						shutil.copy(s_dir, d_dir)
						copy_count += 1
				elif file.endswith('.jpg') or file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.JPEG'):
					if compress_image(s_dir, d_dir, jpg_quality):
						src_file_size = get_file_size(s_dir)
						des_file_size = get_file_size(d_dir)
						perf = round(des_file_size['KB'] / src_file_size['KB'], 2)
						print(Fore.GREEN + '压缩成功!  源文件为:' + s_dir + ' 导出文件为:' + d_dir + "--->文件大小:" + str(
							des_file_size['KB']) + "KB" + "  压缩率为:" + str(perf))
						sort_list.append(des_file_size['KB'])
						s_file.write(s_dir + '\n')
						s_count += 1
					else:
						print(Fore.RED + "jpg或者jpeg图片转化失败，源文件路径为:" + s_dir + "源文件直接复制！")
						shutil.copy(s_dir, d_dir)
						f_file.write(s_dir + '\n')
						copy_count += 1
				elif file.endswith('.svg') or file.endswith('.SVG'):
					svg_command = default_svg_command
					command_args = {'svg_command': svg_command, 'svg_config_file': svg_config_file, 's_dir': s_dir,
									'd_dir': d_dir}
					svg_command = "{svg_command} --config={svg_config_file} {s_dir} -o {d_dir}".format(**command_args)
					if exec_system_command(svg_command) == 0:
						src_file_size = get_file_size(s_dir)
						des_file_size = get_file_size(d_dir)
						perf = round(des_file_size['KB'] / src_file_size['KB'], 2)
						print(Fore.GREEN + '压缩成功!  源文件为:' + s_dir + ' 导出文件为:' + d_dir + "--->文件大小:" + str(
							des_file_size['KB']) + "KB " + "  压缩率为:" + str(perf))
						sort_list.append(des_file_size['KB'])
						s_file.write(s_dir + '\n')
						s_count += 1
					else:
						print(Fore.RED + "svg图片转化失败，源文件路径为:" + s_dir + "源文件直接复制！")
						f_file.write(s_dir + '\n')
						shutil.copy(s_dir, d_dir)
						copy_count += 1
	print(Fore.YELLOW + '总文件数量:' + str(all_count), Fore.GREEN + "  压缩成功图片数量:" + str(s_count),
		  Fore.WHITE + "  直接复制图片数量:" + str(copy_count), Fore.RED + "  压缩失败图片数量:" + str(f_count))
	sort_list.sort()
	print(Fore.RED + "最大文件为：" + str(sort_list[-1]) + "KB" + Fore.GREEN + "      最小文件为：" + str(sort_list[0]) + "KB")
	s_file.close()
	f_file.close()
	all_file.close()
