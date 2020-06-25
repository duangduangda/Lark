#! /usr/bin/env python
import numpy as np
import pandas as pd


def main():
	df = pd.DataFrame(np.random.rand(10, 5), columns = list('ABCDE'))
	print(df)
	print(df.sort_values('A', ascending = False))


if __name__ == '__main__':
	main()
