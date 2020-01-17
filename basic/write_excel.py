#! /usr/bin/env python

import xlwt


def main():
    wr = xlwt.Workbook()
    # 设置sheet名称
    sheet = wr.add_sheet('new_text')
    # 写入新值
    sheet.write(0, 0, 'test')
    # 保存文件
    wr.save('resources/new_text.xlsx')


if __name__ == "__main__":
    main()
