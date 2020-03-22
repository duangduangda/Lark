#! /usr/bin/env python

import os


def check_dir_exists(path):
	if os.path.exists(path):
		print("yes")
	else:
		print("no")


def check_file_type(path):
	if os.path.isdir(path):
		print(path + " is a directory.")
	elif os.path.isfile(path):
		print(path + " is a file.")
	else:
		print("unknown file type.")


def main():
	check_dir_exists('/usr/bin')
	check_file_type('/usr/bin')


if __name__ == '__main__':
	main()
