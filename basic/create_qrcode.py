#! /usr/bin/env python

import qrcode

text = input("输入文字或者URL：")
img = qrcode.make(text)
img.save('eve.png')
img.show()
