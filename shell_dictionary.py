import urllib
import json

import os
title=os.environ["word"]

#title = raw_input("Enter the word to search: ")
print "Word: ", title

try:

	# forming the url to access the api
	url = 'http://glosbe.com/gapi/translate?from=eng&dest=eng&format=json&phrase='+title+'&pretty=true'

	result = json.load(urllib.urlopen(url))

	print "Meaning: ", result["tuc"][0]["meanings"][0]["text"]

except KeyError:
	print "\rSorry That word is not found."