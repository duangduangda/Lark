#! /usr/bin/env python

import numpy as np
import pandas as pd


def main():
	print(pd.__version__)
	print(np.__version__)
	a = np.arange(10)
	print(a)
	s = pd.Series(a)
	print(s)
	

if __name__ == '__main__':
	main()
