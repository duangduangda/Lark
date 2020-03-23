#! /usr/bin/env python

from datetime import datetime


def main():
	# 构造datetime对象
	my_datetime = datetime(2020, 3, 22, 22, 28, 46)
	print(my_datetime)
	# 返回date
	print(my_datetime.date())
	# 返回time
	print(my_datetime.time())
	# 返回timestamp
	print(my_datetime.timestamp())
	# 返回星期(星期一为0，星期天为6)
	print(my_datetime.weekday())
	# 返回星期(星期一为 1，星期天为 7)
	print(my_datetime.isoweekday())


# 返回time


if __name__ == '__main__':
	main()
