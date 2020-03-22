# ！ /usr/bin/env python
import openpyxl

new_workbook = openpyxl.load_workbook('../resources/academy_template.xlsx')
new_sheet = new_workbook['Sheet1']
new_sheet['A3'] = '人工智能学院'
new_sheet['B3'] = '统计分析'
new_sheet['A4'] = '大数据学院'
new_sheet['B4'] = 'Hadoop'
new_workbook.save('../resources/new_course.xlsx')
