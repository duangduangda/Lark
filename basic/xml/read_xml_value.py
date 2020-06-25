#! /usr/bin/env python

import requests


def main():
	response = requests.get('http://planet.python.org/rss20.xml')
	print(response.json())


if __name__ == '__main__':
	main()
