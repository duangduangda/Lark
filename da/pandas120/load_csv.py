#! /usr/bin/env python

import pandas as pd


def load_csv():
	data = pd.read_csv('example_data.csv')
	print(type(data))
	print(data)


if __name__ == '__main__':
	load_csv()
