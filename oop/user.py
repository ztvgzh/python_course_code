class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    def change_name(self, new_name):
        self.name = new_name

    def get_user_info(self):
        print(f"User {self.name} has this {self.email} email")

