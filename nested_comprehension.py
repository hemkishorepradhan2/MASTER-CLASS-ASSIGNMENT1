orders = [
    {"user_id": 1, "items": ["Laptop", "Mouse"]},
    {"user_id": 3, "items": ["Phone", "Charger"]}
]

all_items = [item for o in orders for item in o["items"]]
print(all_items)