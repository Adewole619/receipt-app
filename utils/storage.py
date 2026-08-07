import sys
import json
import os

RECEIPT_FILE = "data/receipts.txt"
RECEIPT_FILE_JSON = "data/receipts.json"


def save_all_receipts(receipts):
    with open(RECEIPT_FILE_JSON, "w") as file:
        json.dump(receipts, file, indent=4)


def load_receipts_json():
    try:
        with open(RECEIPT_FILE_JSON, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No receipts have been saved yet.")
        return []