#! /usr/bin/env python

import pandas as pd


def dump_data_to_json():
	data = pd.read_csv('example_data.csv')
	data.to_json('example_data.json')


if __name__ == '__main__':
	dump_data_to_json()
