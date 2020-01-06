#! /usr/bin/env python
import calendar


def main():
    """
        calendar.prcal() 效果等同print(calendar.calender(2020))
        calendar.pmonth() 效果等同print(calendar.month(2019,1))
    """

    # 按年制作日历
    calendar.prcal(2020)
    print(30 * "**")
    calendar.prmonth(2020, 1)
    print(30 * "*")
    # 判断是否是闰年
    print(calendar.isleap(2020))
    # 判断某月工多少天，从周几开始
    print(calendar.monthrange(2020, 1))
    # 计算某天是周几，返回0~6,标识周一到周日
    print(calendar.weekday(2020, 1, 3))


if __name__ == "__main__":
    main()
