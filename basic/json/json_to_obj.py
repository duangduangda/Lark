#! /usr/bin/env python

import json


class JSONObject(object):
	def __init__(self, d):
		self.__dict__ = d


def main():
	s = '{"name":"eric","share":50,"price":490.1}'
	data = json.loads(s, object_hook = JSONObject)
	print(type(data))
	print(data.name)
	print(data.price)


if __name__ == '__main__':
	main()
