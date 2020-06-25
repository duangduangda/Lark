#! /usr/bin/env python

import time
from threading import Thread


def count_down(n: int):
	while n > 0:
		print('T-minus', n)
		n -= 1
		time.sleep(1)


def main():
	t = Thread(target = count_down, args = (10,))
	t.start()


if __name__ == '__main__':
	main()
