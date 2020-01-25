#! /usr/bin/env python

from xlutils.copy import copy
import xlrd
import xlwt

# 打开模板文件
"""
    此处需要注意，如果要打开的excel文件的后缀是xlsx格式的，在使用formatting_info时会报错。NotImplementedError: formatting_info=True not yet implemented
"""
temp_excel = xlrd.open_workbook(
    'resources/course_template.xls', formatting_info=True)

# 找到工作表
temp_sheet = temp_excel.sheet_by_index(0)

# 复制
new_excel = copy(temp_excel)
# 创建新的sheet
new_sheet = new_excel.get_sheet(0)
# 不带格式写入数据
# new_sheet.write(2, 1, 12)
# new_sheet.write(3, 1, 10)
# new_sheet.write(4, 1, 19)
# new_sheet.write(5, 1, 15)
# new_sheet.write(6, 1, 16)
# new_sheet.write(7, 1, 17)
# new_excel.save('resources/course.xls')

# 自定义样式
style = xlwt.XFStyle()
# 设置字体
font = xlwt.Font()
font.name = '微软雅黑'
font.bold = True
font.height = 360

style.font = font
# 设置边框
borders = xlwt.Borders()
borders.top = xlwt.Borders.THIN
borders.bottom = xlwt.Borders.THIN
borders.left = xlwt.Borders.THIN
style.borders = borders

# excel对齐
aligment = xlwt.Alignment()
aligment.horz = xlwt.Alignment.HORZ_CENTER
aligment.vert = xlwt.Alignment.VERT_CENTER
style.alignment = aligment

# 写入excel
new_sheet.write(2, 1, 12, style)
