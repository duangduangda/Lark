#! /usr/bin/env python

import pandas as pd


def main():
	data = {'工资': [100, 2000, 3000], '绩效': [64, 80, 95], '备注': ['不及格', '良好', '优秀']}
	df = pd.DataFrame(data, index = ['张三', '李四', '王五'])
	# 使用索引，第一个位置标识行索引，第二个位置为列索引,索引取值含首不含尾
	# 获取行索引小于2的行以及列索引小于1的列
	print(df.iloc[:2, :1])
	# 第二行第一列
	print(df.iloc[1:2, 0:1])
	
	# 基于名称的索引
	# 查找工资为2000的行，并打印
	print(df.loc[df['工资'] == 2000, :])
	
	# 获取所有人的工资，行索引使用:
	print(df.loc[:, ['工资', '备注']])
	
	# 获取工资为2000和3000的行，输出工资和备注列
	print(df.loc[df['工资'].isin([2000, 3000]), ['工资', '备注']])
	
	# 求平均工资
	print(df['工资'].mean())
	# 工资方差
	print(df['工资'].std())
	# 中位数
	print(df['工资'].median())
	# 最大值
	print(df['工资'].max())
	# 最小值
	print(df['工资'].min())


if __name__ == '__main__':
	main()
