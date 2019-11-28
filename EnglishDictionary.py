import json

data = json.load(open("data.json"))

word = input("Enter your word:")

print(data[word])
