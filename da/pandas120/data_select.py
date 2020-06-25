# ！ /usr/bin/env python

import numpy as np
import pandas as pd


def main():
	df = pd.DataFrame(np.random.rand(5, 5), columns = list('ABCDE'))
	print(df)
	# 打印C列
	print(df['C'])
	# 打印B，E
	print(df[['E', 'B']])
	# 按照位置取
	s = pd.Series(df['C'])
	print(s.iloc[0])
	# 按照索引取
	print(s.loc[2])
	# 选取第一行
	print(df.iloc[0, :])


if __name__ == '__main__':
	main()
