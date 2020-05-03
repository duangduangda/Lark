#! /usr/bin/env python

import pandas as pd


def main():
	df = pd.read_csv('region.csv')
	# 查看前10行
	print(df.head(10))
	# 查看后10行
	print(df.tail(10))
	# 查看格式
	df.info()
	print(df.describe())


if __name__ == '__main__':
	main()
