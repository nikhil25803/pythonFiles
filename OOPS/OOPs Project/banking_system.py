# Parent Class
class User():

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def show_details(self):
        print(f"User Details: ")
        print(f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}")


# Child CLass
class Bank(User):

    def __init__(self, name,age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self,amount):
        self.amount =  amount
        self.balance = self.balance + self.amount
        print("Account balance have been Updated: ", self.balance)

    def withdrawl(self,amount):
        self.amount = amount
        if self.amount > self.balance :
            print("Insufficient Funds")
            print("Available Balance: ", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance have been updated: ", self.balance)

        def view_balance(self):
            self.show_details()
            print("Account balance have been updated: ", self.balance)

nikhil = Bank("Nikhil", 18, "Male")
nikhil.deposit(500)
nikhil.withdrawl(459)
# nikhil.withdrawl(50)
nikhil.show_details()