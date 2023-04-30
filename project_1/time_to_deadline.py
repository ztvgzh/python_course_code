from datetime import *

user_input = input("Please, enter your goal and deadline separated by colon: \n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]
deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today = datetime.today()
days = deadline_date-today

hours_till = int(days.total_seconds()/60/60)
print(f"Dear user, time remainig for {goal} {hours_till} hours")