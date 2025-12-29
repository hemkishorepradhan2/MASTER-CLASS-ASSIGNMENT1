import json
users = [
    {"id": 1, "name": "Alice", "age": 22, "country": "USA", "active": True,  "spent": 1200},
    {"id": 2, "name": "Bob",   "age": 17, "country": "India", "active": False, "spent": 300},
    {"id": 3, "name": "Carol", "age": 30, "country": "USA", "active": True,  "spent": 2200},
    {"id": 4, "name": "Dave",  "age": 25, "country": "India", "active": True,  "spent": 900},
]
with open("users.json", "w") as f:
    json.dump(users, f, indent=2)

with open("users.json") as f:
    data = json.load(f)
    print(data)
