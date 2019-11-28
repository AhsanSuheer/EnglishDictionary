import json

data = json.load(open("data.json"))

def fetch(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.upper() in data: #For case where word might be an acronym
        return data[word.upper()]
    elif word.title() in data: #For cases where word is a proper noun
        return data[word.title()]
    else:
        return "Sorry, the word was not found in the dictionary."



word = input("Enter your word:")

print(fetch(word))
