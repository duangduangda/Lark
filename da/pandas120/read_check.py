#! /usr/bin/env python

import numpy as np
import pandas as pd


def main():
	s = pd.Series([1, 2, 3, 3, 4, np.nan, 5, 5, 5, 6, 7])
	print(s.value_counts(dropna = False))
	print(s.value_counts(dropna = True))


if __name__ == '__main__':
	main()
