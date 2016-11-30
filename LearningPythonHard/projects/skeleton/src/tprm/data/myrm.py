#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time 
import sys
import os
import shutil
PATH_TRASH = '/home/tuopan/.trash'
def main():
	'''
	myrm file1 file2 file3
	myrm dir1
	argv[0]:myrm
	argv[1]:file1
	argv[2]:file2
	argv[3]:file3
	os.path:处理目录相关操作
	time.time():获取系统时间
	'''
	if len(sys.argv)<2:
		print ('this tool like rm')
		print (sys.argv[0],'file1')
	for arg_file in sys.argv[1:]:
		filename = str(time.time()).split('.')[0]+arg_file
		shutil.move(arg_file,os.path.join(PATH_TRASH,filename))
if __name__ == '__main__':
	if not os.path.exists(PATH_TRASH):
		os.mkdir(PATH_TRASH)
	main()
