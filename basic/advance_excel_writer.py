#! /usr/bin/env python

import xlsxwriter as xw
import xlwt

workbook = xlwt.Workbook()
new_sheet = workbook.add_sheet('sheet0')
for i in range(0, 100):
    new_sheet.write(0, i, i)
workbook.save('num.xls')

"""
    报错，因为在97-03版本的excel文件，不允许列数大于256
"""
workbook = xw.Workbook('resources/numbers.xlsx')
new_sheet = workbook.add_worksheet('sheet0')
for i in range(100):
    new_sheet.write(0, i, i)

workbook.close()
