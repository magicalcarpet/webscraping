# we are going to go to a webpage and store its text in a list and then report the 
# frequencies of the words in that list.

# I need to find a way to scape a given webpage, store its text in a list
# then find a way to count the frequency of each word in that list and the present
# the word count for each word.

# I am gonna use the client 'requests' 

import requests
import pprint
import re

response = requests.get('https://poetrydb.org/author/ambrose')
# print(response.status_code)
# pprint.pprint(response.content)
# pprint.pprint("Hello pretty printer")

# print(response.headers['content-type'])
# pprint.pprint(response.json()[-1]['lines'])
poem_list = response.json()[-1]['lines']
# print(len(poem_list))

joined_poem = ' '.join(poem_list)
# print(joined_poem)

single_spaced_poem = re.sub('(\s{2})', ' ', joined_poem)
punc_removed_poem = re.sub('([,.;])', "", single_spaced_poem).lower().split()

def word_count(chosen_word):
    matched_word = 0
    for word in punc_removed_poem:
        if word == chosen_word:
            matched_word += 1
    return {chosen_word: matched_word}
    # take a list of words
    # cycle through it to count
    # a given word's frequency
    # store that value to be used later


print(word_count('her'))



