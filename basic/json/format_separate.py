#! /usr/bin/env python

import json


def main():
	x = {
		"name": "Bill",
		"age": 63,
		"married": True,
		"divorced": False,
		"children": ("Jennifer", "Rory", "Phoebe"),
		"pets": None,
		"cars": [
			{"model": "Porsche", "mpg": 38.2},
			{"model": "BMW M5", "mpg": 26.9}
		]
	}
	# python to json
	print(json.dumps(x))
	# format
	print(json.dumps(x, indent = 4))
	# change default seperator
	print(json.dumps(x, indent = 4, separators = ('.', '=')))
	# sort by key
	print(json.dumps(x, indent = 4, sort_keys = True))


if __name__ == '__main__':
	main()
