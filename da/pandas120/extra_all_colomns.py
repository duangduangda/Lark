#! /usr/bin/env python
import pandas as pd


def main():
	df = pd.read_csv('example_data.csv')
	# 抽取所有列名
	print(df.columns)


if __name__ == '__main__':
	main()
