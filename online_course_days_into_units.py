"""def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days*24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days*24*60} minutes"
    else:
        return "unsupported unit"
        """
calculation_to_units = 24
name_of_unit = "hours"
def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

def validate_and_execute():
    try:
        user_input_num = int(num_of_days_element)
        if user_input_num > 0:
            calculated_value = days_to_units(user_input_num)
            print(calculated_value)
        elif user_input_num == 0:
            print("you intered a 0, please inter a valid positive number")
        else:
            print("you intered a negative number, no convention for you!")
    
    except ValueError:
        print("your input is not a valid number, do not ruin my program!")

user_input = ""
while user_input != "exit":
    user_input = input("Hey, inter your number:\n")
    list_of_days = user_input.split(",")
    for num_of_days_element in set(list_of_days):
        validate_and_execute()

