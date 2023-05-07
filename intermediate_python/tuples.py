mytuple = ("Max", 28, "Boston")
mytuple1 = ('a', 'r', 'u', 'p', 'e', 'p')
mytuple2 = tuple(["max", 28, "boston"])
print(type(mytuple2))

"""for x in mytuple:
    print(x)"""

if "Max" in mytuple:
    print("yes")
else:
    print("no")

#print(len(mytuple1))
#print(mytuple1.count('p'))
#print(mytuple1.index('e'))

my_tuple = "Gulshad", 24, "Nukus"
name, age, city = my_tuple
#print(f"{name}\n{age}\n{city}")

my_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
i1, *i2, i3 = my_tup
print(f"{i1}\n{i2}\n{i3}")