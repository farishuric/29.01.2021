import csv

class Check:
    def __init__(self,name,pasword):
        self.name = name
        self.pasword = pasword
class Limit(Check):
    def __init__(self,name,password):
        super().__init__(name,password)

    def provjera(self):
        with open('base.csv','r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            for row in csv_reader:
                if self.name == row['name'] and self.pasword == row['pas']:
                    print(row['name'],"Vas limit iznosi",row['limit'])
                    break
                else:
                    print("Hamoooooo")
                    break
while True:
    username = input("Please enter your username: ")
    password = input("Please enter your password: ") 
    haris=Limit(username,password)
    haris.provjera()