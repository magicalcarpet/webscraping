# we are going to go to a webpage and store its text in a list and then report the 
# frequencies of the words in that list.

# I need to find a way to scape a given webpage, store its text in a list
# then find a way to count the frequency of each word in that list and the present
# the word count for each word.

# I am gonna use the client 'requests' 

import requests
import pprint

response = requests.get('https://poetrydb.org/author/ambrose')
print(response.status_code)
# pprint.pprint(response.content)
# pprint.pprint("Hello pretty printer")

# print(response.headers['content-type'])
pprint.pprint(response.json()[-1]['lines'])


