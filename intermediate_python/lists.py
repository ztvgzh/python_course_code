my_list = list()
my_list2 = [1, "apple", True]
my_list3 = ["banana", "lemon", "cucumber", "potato", "watermelon"]

item = my_list3[-2]
#print(item)
#using .append to add an element
my_list3.append("cherry")

#using .insert to add an element to definite place
my_list3.insert(0, "blueberry")
#print(my_list3)

#using .pop to delete last element
my_list3.pop()
#print(my_list3)

#using .remove to delete definite element
my_list3.remove("lemon")
#print(my_list3)

#using .clear to remove all  elements
my_list3.clear()
#print(my_list3)

my_list4 = ["banana", "lemon", "cucumber", "potato", "watermelon"]
# using .reverse to reverse list
my_list4.reverse()
#print(my_list4)

lst = [-5, 2, -10, 6, 8, 3, 0]
#using sord methods
lst.sort()
new_lst = sorted(lst)
print(f"{lst}\n{new_lst}")