import json
from difflib import get_close_matches

#Open JSON file
data = json.load(open("data.json"))


# Search function
def translate(w):
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        return "Did you mean %s instead?" % get_close_matches(w, data.keys())[0]    
    else:
        return "The word does not exist. Check your spelling"


# user Input
word = input("Enter word: ")

print(translate(word.lower()))
