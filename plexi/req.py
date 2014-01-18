
from pprint import pprint
import requests
import unirest

def getNounStr(post):
	r = requests.post("https://stremor-stremor-noun-phrases.p.mashape.com/noun-phrases",
	  
	  headers={
	    "X-Mashape-Authorization": "X8EXpIQOvQeFtzKB7KDpdqnOYRgIFrSP",
	    "Content-Type": "application/json"
	  },
	  data="{\"content\":\"%s\"}" % post
	);
	print post
	print r.code
	pprint(r.body)
	print r.json().get('data', False)
	nouns = r.json().get('data', False)
	if nouns:
		nouns = nouns.get('noun_phrases', False);
	else:
		return ''
	retStr = ""
	for np in nouns:
		retStr += np['noun_phrase']+" ";
	return retStr.strip()


with open('tweets.txt') as f:
    content = f.readlines()
    for line in content:
		parts = line.split(',',1)
		#pprint(parts)
		nouns = getNounStr(u'you are an ugly ass');
		print nouns