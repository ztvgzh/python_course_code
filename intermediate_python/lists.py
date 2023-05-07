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
#print(f"{lst}\n{new_lst}")

#using * to increase in ... times elements
#print(lst*2)

#using slicing
a = lst[2:6]
#print(a) here a sorted list 
list_n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = list_n[::2] #index: 0(first index to start) 2 4 6 8: [1, 3, 5, 7, 9] 
b2 = list_n[::3] #index: 0 3 6 9: [1, 4, 7, 10]
#print(b)

#copying to new list
list_new = list(list_n)
list_new1 = list_n.copy()
# list_new2 = list_n they will use one memory 
list_new3 = list_n[:]
list_new.append(1)
list_new1.append(3)
#list_new2.append(7) 
list_new3.append(8)
#print(f"{list_n}\n{list_new}\n{list_new1}")

c = [i*2 for i in list_n] #[i*i for i in list_n]
print(c)

