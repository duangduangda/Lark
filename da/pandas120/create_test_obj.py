#! /usr/bin/env python

import numpy as np
import pandas as pd


def main():
	df = pd.DataFrame(np.random.rand(10, 5))
	df.index = pd.date_range('2020-06-24', periods = df.shape[0])
	print(df.head(2))
	print(df.tail(1))


if __name__ == '__main__':
	main()
