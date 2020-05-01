#! /usr/bin/env python

import json

import pandas as pd
import requests


def get_city_info(url):
	data = []
	response = requests.get(url)
	json_dict = json.loads(response.text)
	provinces = json_dict['data']['provinces']
	for province in provinces:
		data.append([province['code'], province['name']])
		cities = province['cities']
		for city in cities:
			data.append([city['code'], city['name']])
	return data


def main():
	data = get_city_info('ftp://gis/list')
	df = pd.DataFrame(data)
	df.to_excel('城市信息.xlsx', sheet_name = '城市信息')


if __name__ == '__main__':
	main()
