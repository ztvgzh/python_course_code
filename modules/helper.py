def days_to_unit(number_of_days, convertion_unit):
    if convertion_unit == "hours":
         return f"{number_of_days} days are {number_of_days*24} hours"
    elif convertion_unit == "minutes":
         return f"{number_of_days} days are {number_of_days*24*60} minutes"
    elif convertion_unit == "seconds":
         return f"{number_of_days} days are {number_of_days*24*60*60} seconds"
    else:
         return "unsupported unit"


def validate_and_execute():
    try:
        user_input_number = int(days_and_unit_dict["days"])
        if user_input_number > 0:
            calculated_value = days_to_unit(user_input_number, days_and_unit_dict["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("You intered 0, change number of days!")
        else:
            print("You intered negative number, change number of days!")
    except ValueError:
            print("Don't ruin my program!")