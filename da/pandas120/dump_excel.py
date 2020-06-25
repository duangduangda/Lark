#! /usr/bin/env python

import pandas as pd


def dump_to_excel():
    data = pd.read_csv('example_data.csv')
    data.to_excel('example_data.xlsx')


if __name__ == '__main__':
    dump_to_excel()
