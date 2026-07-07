import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exists")
    except Exception as err:
        print(f"An exception occurs as {err}")

    @staticmethod
    def __update():
        with open(Bank.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k = 3)
        num = random.choices(string.digits, k = 3)
        spchar = random.choices("!@#$%^&*", k = 1)
        id = alpha + num + spchar
        random.shuffle(id)
        return"".join(id) 

         
    def createaccount(self):
        info = {
            "name": input("What is your Name: "),
            "age": int(input("What is your Age: ")),
            "email": input("Write email: "),
            "pin": int(input("Write your 4 numbers pin code: ")),
            "accountNo.": Bank.__accountgenerate(),
            "balance": 0
        }
        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("Sorry you cannot create your account")
        else:
            print("Account has been created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("note down your account number")

            Bank.data.append(info)

            Bank.__update()

    def depositmoney(self):
        accnumber = input("please tell your accounnt number: ")
        pin = int(input("Tell your 4 number pin: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry o data found")

        else:
            amount =  int(input("How much you want to Depsit "))
            if amount >   10000 or amount < 0:
                print("Sorry the amount is too much you can deposite below 10,000 abd above 0")
            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Amount deposited successfully")

    def withdrawmoney(self):
        accnumber = input("please tell your accounnt number: ")
        pin = int(input("Tell your 4 number pin: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry o data found")

        else:
            amount =  int(input("How much you want to Witdraw: "))
            if userdata[0]['balance'] <  amount:
                print("You don't have that much money" )
              
            else:
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("Amount Withdraw successfully")

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

if check == 2:
    user.depositmoney()

if check == 3:
    user.withdrawmoney()
