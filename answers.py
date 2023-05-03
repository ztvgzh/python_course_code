"""
#   TASK 1
import tldextract as t

# Get URL from user
url = input("Enter URL: ")
 
# Extract information from URL
domain_name_extract = t.extract(url)

# Print only the domain name
print("Domain name is:", domain_name_extract.domain)
"""




"""
#   TASK 2
import array as a

# Get numbers from user
user_input = input("Enter your numbers: \n")
# reverse string parameters into int
list = user_input.split(",")
# create new array
arr1 = a.array('i')
# variable for keeping numbers of zeros
num_zero = 0

# loop for adding list elements into array
for i in range(len(list)):
    arr1.append(int(list[i]))
# loop for finding and deleting zeros in array
for number in arr1:
    if number == 0:
        arr1.remove(number)
        num_zero+=1
# loop for adding that quantity of zeros which we deleted below to the end of array
for i in range(num_zero):
    arr1.append(0)

# printing result
print(f"New array: {arr1}")
"""




"""
# TASK 3
user_input = input("Enter your message: \n")

if len(user_input) > 140 or len(user_input) == 0:
    print("False")
else:
    print(f"#{user_input}")
"""