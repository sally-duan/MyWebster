import json
with open('.\data.json') as f:
    data = json.load(f)

print("The data type is {}".format(type(data)))
p=0
for key, value in data.items():
    p=p+1
print("There are {} words in this dictionary".format(p))

def FindWordDefinition(word):
    word =word.lower()
    if word in data:
        return data[word]
    else:
        print("Sorry we could not find the word in this dictionary")
        pass


word =input("Type what you want to know, for example, rain: ")
print(FindWordDefinition(word))

