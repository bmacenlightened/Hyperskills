water = 400
milk = 540
beans = 120
cups = 9
money = 550
machine_phrase = "The coffee machine has:"

def display_machine():
    print(f"{machine_phrase}\n{water} of water\n{milk} of milk\n{beans} of beans\n{cups} of cups\n{money} of money\n\n")

def select_action() -> str:
    return input('Write action (buy, fill, take, remaining, exit): ')
    
def pick_drink() -> int:
    print()
    response = input('What do you want to buy?'
                     ' 1 - espresso,'
                     ' 2 - latte,'
                     ' 3 - cappuccino,'
                     ' back - to main menu: ')
    if response == 'back':
        return 0
    return int(response)
    
def can_make(need_water=0, need_milk=0, need_beans=0):
    if water < need_water:
        print('Sorry, not enough water!\n')
        return False
    if milk < need_milk:
        print('Sorry, not enough milk!\n')
        return False
    if beans < need_beans:
        print('Sorry, not enough beans!\n')
        return False
    if cups < 1:
        print('Sorry, not enough cups\n')
        return False
    print('I have enough resources, making you a coffee!\n')
    return True
    
def buy():
    global water, milk, beans, cups, money
    drink = pick_drink()
    if drink == 1:  # espresso
        if can_make(need_water=250, need_beans=16):
            money += 4
            water -= 250
            beans -= 16
            cups -= 1
    elif drink == 2:  # latte
        if can_make(need_water=350, need_milk=75, need_beans=20):
            money += 7
            water -= 350
            milk -= 75
            beans -= 20
            cups -= 1
    elif drink == 3:  # cappuccino
        if can_make(need_water=200, need_milk=100, need_beans=12):
            money += 6
            water -= 200
            milk -= 100
            beans -= 12
            cups -= 1
    else:
        print("Invalid choice")
        pass
    
def fill():
    global water, milk, beans, cups
    water += int(input('\nWrite how many ml of water do you want to add:\n'))
    milk += int(input('Write how many ml of milk do you want to add:\n'))
    beans += int(input('Write how many grams of coffee beans do you want to add:\n'))
    cups += int(input('Write how many disposable cups of coffee do you want to add:\n'))
    print()

def take():
    global money
    print(f'\nI gave you ${money}\n')
    money = 0

def main():
    while True:
        action = select_action()

        if action == 'buy':
            buy()
        elif action == 'fill':
            fill()
        elif action == 'take':
            take()
        elif action == 'exit':
            break
        elif action == 'remaining':
            display_machine()
        else:
            print("Invalid option")


if __name__ == '__main__':
    main()
