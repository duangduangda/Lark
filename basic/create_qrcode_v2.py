#! /usr/bin/env python
import qrcode
'''
制作不同尺寸的二维码
'''

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

qr.add_data('今天是平安夜')
qr.make(fit=True)

img = qr.make_image()
img.save('eve.png')
