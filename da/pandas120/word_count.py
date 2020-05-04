#! /usr/bin/env python

import pandas as pd


def main():
	df = pd.read_csv('example_data.csv')
	# 对列language进行字符统计
	print(df['language'].value_counts())


if __name__ == '__main__':
	main()
