
class Bank:
    def createaccount(self):
        pass

    
user = Bank()

print("Press 1 for Creating an Account")
print("Press 2 for Deposite the money in the Bank")
print("Press 3 for withdraw the money")
print("Press 4 for Deteils")
print("Press 5 to Update the Details")
print("Press 6 for Delete the Account")

check = int(input("Tell your response here: "))

if  check == 1:
    user.createaccount()
