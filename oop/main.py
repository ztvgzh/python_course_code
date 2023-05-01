import user as u

user1 = u.User("Gulshad", "azatova@itmo.ru", "pwd")
user1.get_user_info()

user1.change_name("Gusha")
user1.get_user_info()