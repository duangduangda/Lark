#! /usr/bin/env python
import pandas as pd


def main():
	print(pd.__version__)
	dates = pd.date_range('2020-04-26', periods = 6)
	print(dates)
	print(dates.T)


if __name__ == '__main__':
	main()
