#! /usr/bin/env python

from time import sleep
from time import time
from time import localtime
from time import strftime

'''
    倒计时
'''
 count = 0
  a = int(input('time:'))
   while count < a:
        count_now = a - count
        print(count_now)
        sleep(1)
        count = count + 1
    print('time up')
