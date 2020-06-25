#! /usr/bin/env python

import numpy as np
import pandas as pd


def main():
	df = pd.DataFrame({'A': np.array(['foo', 'foo', 'foo', 'foo', 'bar', 'bar']),
	                   'B': np.array(['one', 'one', 'two', 'two', 'three', 'three']),
	                   'C': np.array(['small', 'medium', 'large', 'large', 'small', 'small']),
	                   'D': np.array([1, 2, 2, 3, 3, 5])})
	print(df.groupby('A').count())
	print(df.groupby(['B', 'C']).sum())
	print(df.groupby('B')['D'].mean())
	print(df.groupby('A').agg(np.mean))


if __name__ == '__main__':
	main()
