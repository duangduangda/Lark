#! /usr/bin/env python

import pandas as pd


def main():
	df = pd.read_csv('region.csv')
	# 新增Pid列
	df['pid'] = range(1, len(df) + 1)
	print(df.head())
	# 获取多列
	print(df[['id', 'name']])
	# 批量修改列值
	df['pid'] = 10
	print(df.head(10))
	# 修改字符串.str
	df1 = df.tail(10)
	df1 = df1['name'].str.replace('地区', '市')
	print(df1)


if __name__ == '__main__':
	main()
