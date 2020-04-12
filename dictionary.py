import json
from difflib import get_close_matches

#Open JSON file
data = json.load(open("data.json"))


# Search function
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])    
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn =="N":
            return "This word does not exist, please check your spelling"
        else:
            return "We did not understand your entry. Try again"    
    else:
        return "The word does not exist. Check your spelling"


# user Input
word = input("Enter word: ")

# Output
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)