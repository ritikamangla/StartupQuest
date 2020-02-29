import json
'''
posts = []
with open('news.json', 'r') as f:
		posts = json.load(f)'''
def newsfun():
	posts = []
	with open('news.json', 'r') as f:
		posts = json.load(f)

	return posts


#print(posts)
