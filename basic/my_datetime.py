#! /usr/bin/env python

import datetime


def main():
    # 获取当前时间
    print(datetime.datetime.now())
    print(datetime.datetime.today())
    # 设置格式
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # 时间加减法
    today = datetime.datetime.now()
    # 昨天同一时间
    print(today - datetime.timedelta(days=1))
    # 下周同一时间
    print(today + datetime.timedelta(weeks=1))


if __name__ == "__main__":
    main()
