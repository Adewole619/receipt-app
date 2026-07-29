import json

receipt = {
    "store": "Shoprite",
    "grand_total": 3000,
}

json_string = json.dumps(receipt, indent=4)

# with open("data/receipts.json", "w") as file:
#     json.dump(receipt, file, indent = 4)

# with open("data/receipts.json", "r") as file:
#     receipt = json.load(file)
receipts = json.loads(json_string)
print(receipts)