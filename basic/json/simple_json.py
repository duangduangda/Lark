#! /usr/bin/env python

import json


def main():
	data = {
		"president": {
			"name": "G W Bush",
			"species": "Betelgeusian"
		}
	}
	# write to file
	# dump/load和文件组合使用，dumps将json转化为字符串，loads则刚好相反
	with open('data_file.json', 'w') as target:
		json.dump(data, target)
	json_str = json.dumps(data, indent = 4)
	print(json_str)


if __name__ == '__main__':
	main()
