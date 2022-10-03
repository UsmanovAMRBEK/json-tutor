import json


file = open('data.json', 'r',encoding="utf8")
data = json.load(file)
# print(type(data))

names = []
for item in data["messages"]:
    if item["type"]=="message" and item["from"]!=None:
        names.append(item["from"])

print(len(set(names)))
