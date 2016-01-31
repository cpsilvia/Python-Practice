#!/usr/bin/env/ python

import argparse
import fnmatch
import os
import shutil

f = open('out.txt', 'w')

def copy_files(root_dir, dest_dir, extension_list):
	for dir_name, sub_dir_list, file_list in os.walk(root_dir):
		f.write('Found directory: %s\n' % dir_name)
		for extension in extension_list:
			for filename in fnmatch.filter(file_list, '*.' + extension):
				f.write('\t%s\n' % os.path.join(dir_name, filename)) 
				shutil.copy(os.path.abspath(dir_name + '/' + filename), dest_dir)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('root_directory')
	parser.add_argument('destination_directory')
	parser.add_argument('extension_list', nargs='+')
	args = parser.parse_args()
	copy_files(args.root_directory, args.destination_directory, args.extension_list)
	
if __name__ == '__main__':
	main()

