#! /usr/bin/env python

import xlrd


def main():
    wr = xlrd.open_workbook('resources/test.xlsx')
    sheet_by_index = wr.sheet_by_index(0)
    print(sheet_by_index.cell_value(1, 1))


if __name__ == "__main__":
    main()
