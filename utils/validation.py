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