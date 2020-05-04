# ！/usr/bin/env python

import pandas as pd


def main():
	df1 = pd.DataFrame({'A': [1, 2, 3]}, index = [1, 2, 3])
	df2 = pd.DataFrame({'A': [1, 1, 3]}, index = [2, 1, 3])
	# 索引对齐
	print(df1 - df2)
	# 根据索引对齐问题，新增的列的索引是从0开始的，所以新的列，最后一列是NAN
	df1 = df1.assign(C = pd.Series(list('def')))
	print(df1)
	
	# 根据数据类型筛选
	print(df1.select_dtypes(include = ['number']).head())
	
	# Series转化为DataFrame
	s = df1.mean()
	s.name = 'series to dataframe'
	print(s.to_frame())
	
	# 计数
	print(df1['A'].count())
	# 值计数
	print(df1['A'].value_counts())
	
	# 唯一值个数
	print(df2['A'].nunique())
	# 唯一值
	print(df2['A'].unique())
	
	# 获取最大值的索引
	print(df1['A'].idxmax())
	# 获取Top N
	print(df1['A'].nlargest(2))


if __name__ == '__main__':
	main()
