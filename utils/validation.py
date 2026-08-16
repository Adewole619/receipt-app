import sys

def validate_string_input(field_name):
    while True:
        string_input = input(f"Enter {field_name} (or q to quit): ").strip()

        if string_input.lower() == "q":
            print("Program terminated.")
            sys.exit()

        if not string_input:
            print(f"{field_name} can not be empty. Try again.")
            continue
    
        # print(f"{field_name} is stored successfully")
        return string_input

def validate_num_input(field_name, num_type):

    while True:
        int_input = input(f"Enter {field_name} (or q to quit): ").strip()

        if int_input.lower() == "q":
            print("Program terminated.")
            sys.exit()
        try:
            if num_type == int:
                val = int(int_input)
            elif num_type == float:
                val = float(int_input)
            else:
                raise ValueError("num_type must be int or float")

            if val <= 0:
                print(f"{field_name} must be greater than 0. Try again.")
                continue
    
            # print(f"{field_name} is stored successfully.")
            return val
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_menu_choice(prompt):
    return input(prompt).strip()

def get_optional_string_input(prompt):
    return input(prompt).strip()

def validate_phone_number():

    while True:

        phone = get_menu_choice("Enter phone number: ").strip()
        if not phone:
            print("Phone number cannot be empty.")
            continue

        if not phone.isdigit():
            print("Phone number must contain digits only.")
            continue

        if len(phone) != 11:
            print("Phone number must contain 11 digits.")
            continue

        if not phone.startswith("0"):
            print("Phone number must start with 0.")
            continue

        return phone

def validate_optional_phone():

    while True:

        phone = input(
            "New phone (press Enter to keep current): "
        ).strip()

        # Keep the current phone
        if phone == "":
            return ""

        if not phone.isdigit():
            print("Phone number must contain digits only.")
            continue

        if len(phone) != 11:
            print("Phone number must contain 11 digits.")
            continue

        if not phone.startswith("0"):
            print("Phone number must start with 0.")
            continue

        return phone


def validate_optional_string(field_name):

    while True:
        value = input(
            f"{field_name} "
            "(press Enter to keep current value): "
        ).strip()

        # Enter was pressed → keep the current value
        if value == "":
            return ""

        return value