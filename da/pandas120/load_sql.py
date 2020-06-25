#! /usr/bin/env python

import pandas as pd
from sqlalchemy import create_engine


def load_data_from_db():
	db_info = {'user': 'root',
	           'password': 'root',
	           'host': 'localhost:3306',
	           'database': 'test'
	           }
	engine = create_engine('mysql://%(user)s:%(password)s@%(host)s/%(database)s?charset=utf8' % db_info,
	                       encoding = 'utf-8')
	data = pd.read_sql_query('SELECT * FROM `user` t WHERE t.`status` = 10;', con = engine)
	data.to_csv('all_available_user.csv')


if __name__ == '__main__':
	load_data_from_db()
