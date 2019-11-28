import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def fetch(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.upper() in data: #For case where word might be an acronym
        return data[word.upper()]
    elif word.title() in data: #For cases where word is a proper noun
        return data[word.title()]
    elif len(get_close_matches(word, data.keys())) > 0:
        userAns = input(f"Did you mean {get_close_matches(word, data.keys())[0]} instead? Reply 'Y' or 'N'")
        if userAns == 'Y':
            return data[get_close_matches(word, data.keys())[0]] #Returning the closest match
        elif userAns == 'N':        
            return "Sorry, the word was not found in the dictionary."
        else:
            return "Invalid answer."
    else:
        return "Sorry, the word was not found in the dictionary."



word = input("Enter your word:")
answer = fetch(word)

#Dealing with words that have multiple definitions
if type(answer) == list: 
    for definition in answer:
        print(definition)
else:
    print(answer)
