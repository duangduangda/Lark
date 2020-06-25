#! /usr/bin/env python

import numpy as np
import pandas as pd


def main():
	df = pd.DataFrame(np.random.rand(10, 5), columns = list('ABCDE'))
	print(df)
	# 查找A列值大于0.5的行
	print(df[df['A'] > 0.5])
	# 查找C列值大于0.5，D列值小于0.7的行
	print(df[(df['C'] > 0.5) & (df['D'] < 0.7)])


if __name__ == '__main__':
	main()
