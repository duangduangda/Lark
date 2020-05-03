#! /usr/bin/env python

import json


def main():
	leads_user_id = []
	user_id = []
	with open('data', 'r') as f:
		data = json.loads(f.readline())
		for d in data:
			leads_user_id.append(d['userId'])

	with open('user_id', 'r') as f:
		data = f.readline().split(',')
		for d in data:
			user_id.append(int(d))

	print(len(leads_user_id))
	print(len(user_id))

	print([uid for uid in leads_user_id if uid not in user_id])


if __name__ == '__main__':
	main()
