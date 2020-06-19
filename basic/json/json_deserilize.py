#! /usr/bin/env python

import json


def main():
	blackjack_hand = (8, 'Q')
	encode_hand = json.dumps(blackjack_hand)
	encode_hand = json.loads(encode_hand)
	print(encode_hand)
	print(blackjack_hand == encode_hand)
	print(type(blackjack_hand))
	print(type(encode_hand))

	with open('data_file.json', 'r') as file:
		data = json.load(file)
	print(data)

	json_string = """
		{
            "researcher": {
            "name": "Ford Prefect",
            "species": "Betelgeusian",
            "relatives": [
                {
                    "name": "Zaphod Beeblebrox",
                    "species": "Betelgeusian"
                }
            ]
        }
	}
	"""
	json_data = json.loads(json_string)

	print(json_data)


if __name__ == '__main__':
	main()
