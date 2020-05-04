#! /usr/bin/env python

import pandas as pd


def main():
    df = pd.read_table('table.txt')
    print(df)


if __name__ == '__main__':
    main()
