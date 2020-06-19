#! /usr/bin/env python

import json

import requests


def main():
	response = requests.get('https://jsonplaceholder.typicode.com/to_dos')
	to_dos = json.loads(response.text)
	print(to_dos)
	todo_by_user = {}
	# count by each user
	for todo in to_dos:
		if todo['completed']:
			try:
				todo_by_user[todo['userId']] += 1
			except:
				todo_by_user[todo['userId']] = 1

	top_users = sorted(todo_by_user.items(), key = lambda x: x[1], reverse = True)

	max_complete = top_users[0][1]
	users = []
	for user, num_complete in top_users:
		if num_complete < max_complete:
			break
		users.append(str(user))
	max_users = " and ".join(users)
	print(max_users)


if __name__ == '__main__':
	main()
