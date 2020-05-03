#! /usr/bin/env  python

import pandas as pd


def main():
	# 创建dataFrame,如果不指定索引，将按从0开始
	data = {'工资': [100, 2000, 3000], '绩效': [64, 80, 95], '备注': ['不及格', '良好', '优秀']}
	df = pd.DataFrame(data, index = ['张三', '李四', '王五'])
	print(df)


if __name__ == '__main__':
	main()
