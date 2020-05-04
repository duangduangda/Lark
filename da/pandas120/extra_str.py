#! /usr/bin/env python

import pandas as pd


def main():
	df = pd.read_csv('example_data.csv')
	# 查找包含Python字样的行
	print(df.loc[df['language'] == 'Python', :])


if __name__ == '__main__':
	main()
