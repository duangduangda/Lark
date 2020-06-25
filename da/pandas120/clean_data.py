#! /usr/bin/env python

import numpy as np
import pandas as pd


def main():
	df = pd.DataFrame({'A': np.array([1, np.nan, 2, 3, 6, np.nan]),
	                   'B': np.array([np.nan, 4, np.nan, 5, 9, np.nan]),
	                   'C': 'foo'})
	print(pd.isnull(df))
	print(pd.notnull(df))
	# 去除包含空值的行
	print(df.dropna())
	# 去除包含空值的列
	print(df.dropna(axis = 1))
	# 将空值替换成x
	print(df.fillna(100))
	df1 = df.fillna(10)
	# 将所有10替换成one
	print(df1.replace(10, 'one'))
	# 1-》one,2->two
	print(df.replace([1, 2], ['one', 'two']))
	# 列重命名
	print(df.rename(columns = lambda x: x + '2'))
	print(df.rename(columns = {'A': 'A1'}))


if __name__ == '__main__':
	main()
