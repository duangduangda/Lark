#! /usr/bin/env python

import mysql.connector as connector


def main():
    conn = connector.connect(host='rds-dev.com',
                             user='root',
                             passwd='1234',
                             database='test')
    cursor = conn.cursor()
    cursor.execute('desc user')
    for x in cursor:
        print(x)

    cursor.execute(
        'select * from user where id = %d' %
        10024644)
    for x in cursor:
        print(x)


# 只读一条
# unique_row = cursor.fetchone()
# print(unique_row)


if __name__ == '__main__':
    main()
