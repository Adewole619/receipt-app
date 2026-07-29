def generate_receipt_number():
    # # Path to the JSON file where receipts are stored
    # file_name = "data/receipts.json"

    # If the receipts file does not exist, start with the first receipt number
    if not os.path.exists(RECEIPT_FILE_JSON):
        return "RCP0000001"

    try:
        # Open the receipts file and load its contents into a list
        with open(RECEIPT_FILE_JSON, "r") as file:
            receipts = json.load(file)
    except json.JSONDecodeError:
         # File exists but is empty or contains invalid JSON
        return "RCP0000001"

    # If the file exists but contains no receipts, start with the first receipt number
    if len(receipts) == 0:
        return "RCP0000001"

    # Get the most recently added receipt
    last_receipt = receipts[-1]

    # Extract the receipt number (e.g., "RCP0000005")
    last_number = last_receipt["receipt_number"]

    # Remove the "RCP" prefix and convert the remaining digits to an integer
    number = int(last_number.replace("RCP", ""))

    # Increment the receipt number by 1
    number += 1

    # Return the new receipt number with the "RCP" prefix
    # and pad the number with leading zeros to make it 7 digits long
    return f"RCP{number:07d}"

def save_receipt_json(receipt):

    try:
        with open(RECEIPT_FILE_JSON, "r") as file:
            receipts = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        receipts = []

    receipts.append(receipt)

    with open(RECEIPT_FILE_JSON, "w") as file:
        json.dump(receipts, file, indent=4)

def load_receipts_json():
    try:
        with open(RECEIPT_FILE_JSON, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No receipts have been saved yet.")
        return []
