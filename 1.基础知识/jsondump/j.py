import json

num = {'name': 'steveyu', 'age': 18, 'hobby': ['basketball', 'running']}

with open('steveyuInfo', 'w') as f:
    json.dump(num, f)


with open('steveyuInfo', 'r') as f:
    json_obj = json.load(f)
    print(json_obj['name'])