#! /usr/bin/env python
import pandas as pd


def main():
	df = pd.read_csv('example_data.csv')
	# 修改列名language为grammar,inplace为True时将直接修改源文件
	df.rename(columns = {'language': 'grammar'}, inplace = True)
	print(df)


if __name__ == '__main__':
	main()
