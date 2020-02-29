import json

def fun():
	posts = []
	with open('items.json', 'r') as f:
		data_dict = json.load(f)
	posts= []

	#for d in data_dict.values():

	for i in range(len(data_dict["title"])):
		posts.append({'title': data_dict["title"][i], 'description': data_dict["description"][i]})


	return posts
"""
for i in posts:
	print(i)
"""	