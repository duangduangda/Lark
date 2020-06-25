#! /usr/bin/env python

import numpy as np
import pandas as pd


def main():
	df = pd.DataFrame(np.random.rand(10, 5), columns = list('ABCDE'))
	# 求每列的平均值
	print(df.apply(np.mean))
	# 求每行的最大值
	print(df.apply(np.max, axis = 1))


if __name__ == '__main__':
	main()
