#! /usr/bin/env python

import numpy as np
import pandas as pd


def main():
	s = pd.Series(np.random.randn(5), index = ['a', 'b', 'c', 'd', 'e'], name = '这是一个测试series', dtype = 'float64')
	print(s)
	# 获取series名称
	print(s.name)
	# 获取series所有值
	print(s.values)
	# 获取索引列
	print(s.index)


if __name__ == '__main__':
	main()
