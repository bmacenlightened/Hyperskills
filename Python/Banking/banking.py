# Write your code here
import random
import sqlite3

db = sqlite3.connect('card.s3db')
sql = db.cursor()
sql.execute('''CREATE TABLE IF NOT EXISTS card
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            number TEXT, pin TEXT, balance INTEGER DEFAULT 0)''')
db.commit()


class Account:
    def __init__(self, card, pin):
        self.card = card
        self.pin = pin
        self.balance = 0


class Bank:
    def __init__(self):
        self.menu_choice = ''
        self.menu_choice_two = ''
        self.balance = 0
        self.number = 0
        self.pin = 0

    def create_card(self):
        print("\nYour card has been created")
        card_number = str(random.randint(4000000000000000, 4000009999999999))
        while not self.luhn(card_number):
            card_number = str(random.randint(4000000000000000, 4000009999999999))
        print("Your card number:")
        print(card_number);
        pin_code = ''.join(str(random.randint(0, 9)) for _ in range(4))
        print("Your card PIN:")
        print(pin_code)
        print("\n")
        sql.execute(f'INSERT INTO card (number, pin, balance) VALUES({card_number}, {pin_code}, 0)')
        db.commit()

    def login(self):
        print("Enter your card number:")
        in_number = input()
        print("Enter your PIN:")
        in_pin = input()
        sql.execute(f"SELECT * FROM card WHERE number = {in_number} AND pin = {in_pin}")
        row = sql.fetchone()
        if row is not None:
            self.number = row[1]
            self.pin = row[2]
            self.balance = int(row[3])
            print("\nYou have successfully logged in!\n")
        else:
            self.number = None
            self.pin = None
            self.balance = None
            print("\nWrong card number or PIN!\n")

    def add_balance(self):
        print("\nEnter income:")
        money = int(input())
        self.balance = self.balance + money
        sql.execute(f"UPDATE card SET balance={self.balance} WHERE number={self.number}")
        db.commit()
        print("Income was added\n")

    def show_balance(self):
        print(f"\nBalance: {self.balance}\n")

    def luhn(self, card_number):
        last_digital = card_number[-1]
        card_number = card_number[:-1]
        sum_odd = 0
        for x in range(0, 15, 2):
            k = int(card_number[x]) * 2
            if k > 9:
                sum_odd += (k // 10 + k % 10)
            else:
                sum_odd += k
        sum_even = 0
        for y in range(1, 14, 2):
            sum_even += int(card_number[y])
        if last_digital == str((sum_odd + sum_even) % 10) == "0":
            return True
        elif last_digital == str(10 - (sum_odd + sum_even) % 10):
            return True
        return False

    def do_transfer(self):
        print("\nTransfer\nEnter card number:")
        in_card = input()
        if not self.luhn(in_card):
            print("Probably you made mistake in the card number. Please try again!")
        else:
            sql.execute(f"SELECT * FROM card WHERE number = {in_card}")
            row = sql.fetchone()
            if row is None:
                print("Such a card does not exist.")
            else:
                print("Enter how much money you want to transfer:")
                in_money = int(input())
                if in_money > self.balance:
                    print("Not enough money!")
                else:
                    self.balance = self.balance - in_money
                    transfer_balance = int(row[3]) + in_money
                    sql.execute(f"UPDATE card SET balance={self.balance} WHERE number={self.number}")
                    sql.execute(f"UPDATE card SET balance={transfer_balance} WHERE number={row[1]}")
                    db.commit()

    def close_account(self):
        sql.execute(f"DELETE FROM card WHERE number={self.number}")
        db.commit()

    def run(self):
        while True:
            self.menu()
            if self.menu_choice == '1':
                self.create_card()
            elif self.menu_choice == '2':
                self.login()
                if self.balance is not None:
                    while True:
                        self.menu_two()
                        if self.menu_choice_two == '1':
                            self.show_balance()
                        elif self.menu_choice_two == '2':
                            self.add_balance()
                        elif self.menu_choice_two == '3':
                            self.do_transfer()
                        elif self.menu_choice_two == '4':
                            self.close_account()
                            break
                        elif self.menu_choice_two == '5':
                            print(f"\nYou have successfully logged out!\n")
                            break
                        elif self.menu_choice_two == '0':
                            print("\nBye!")
                            exit()
            elif self.menu_choice == '0':
                break
            else:
                print("Not a valid command")
        print("Bye!")

    def menu(self):
        print("1. Create an account\n2. Log into account \n0. Exit")
        self.menu_choice = input()

    def menu_two(self):
        print("1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit")
        self.menu_choice_two = input()

def main():
    bank = Bank()
    bank.run()


if __name__ == '__main__':
    main()
