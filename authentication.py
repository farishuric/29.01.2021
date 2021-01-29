import csv

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    

class Checker(User):
    def __init__(self, username, password):
        super().__init__(username, password)
    def check(self):
        with open("userdb.csv", "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if self.username == row['username'] and self.password == row['password']:
                    print(f"Hello {row['username']}. Your balance is {row['balance']}€.")
                    break
                elif self.username != row['username'] and self.password != row['password']:
                    continue
                else:
                    print("Wrong username or password. Please try again.")
                    break


while True:
    user_name = input("Enter username: ")
    user_password = input("Enter password: ")
    user = Checker(user_name, user_password)
    user.check()