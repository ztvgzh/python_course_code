# import helper
from helper import validate_and_execute

user_input = ""
while user_input != "exit":
    user_input = input("Inter number of days and unit:\n")
    days_and_unit = user_input.split(":")
    days_and_unit_dict = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    validate_and_execute(days_and_unit_dict)