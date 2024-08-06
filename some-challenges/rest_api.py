import requests
import json
import pprint

# curl -sS https://jsonmock.hackerrank.com/api/food_outlets?city=seattle | python -m json.tool

def find_best_restaurant(city,cost):
	'''
	Find restaurant in given city with best user rating and with cost lower that passed parameter
	'''
	result = requests.get(f'https://jsonmock.hackerrank.com/api/food_outlets?city={city}&page=1')
	restaurants = result.json()
	restaurants = restaurants['data']

	filter_by_cost = [x for x in restaurants if x['estimated_cost'] < cost]

	highest_score_restaurants = sorted(filter_by_cost, key=lambda r: (r['user_rating']['votes']), reverse=True)

	print('---')
	for item in highest_score_restaurants:
		print(f'Restaurant: {item["name"]}')
		print(f'Cost: {item["estimated_cost"]}')
		print(f'Votes: {item["user_rating"]["votes"]}')
		print('---')


if __name__ == '__main__':
	
	find_best_restaurant('seattle',200)