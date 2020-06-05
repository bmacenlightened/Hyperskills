water = 400
milk = 540
beans = 120
cups = 9
money = 550
machine_phrase = "The coffee machine has:"

def display_machine():
    print(f"{machine_phrase}\n{water} of water\n{milk} of milk\n{beans} of beans\n{cups} of cups\n{money} of money\n\n")
    
def write_action():
    global water, milk, beans, cups, money
    action = input("Write action (buy, fill, take):\n")
    if action == "buy":
        buy_option = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n"))
        if buy_option == 1:
            water = water - 250
            beans = beans - 16
            money = money + 4
            cups = cups - 1
        elif buy_option == 2:
            water = water - 350
            beans = beans - 20
            milk = milk - 75
            money = money + 7
            cups = cups - 1
        elif buy_option == 3:
            water = water - 200
            milk = milk - 100
            beans = beans -12
            money = money + 6
            cups = cups - 1
    elif action == "fill":
        water = water + int(input("Write how many ml of water do you want to add:\n"))
        milk = milk + int(input("Write how many ml of milk do you want to add:\n"))
        beans = beans + int(input("Write how many grams of coffee beans do you want to add:\n"))
        cups = cups + int(input("Write how many disposable cups of coffee do you want to add:\n"))
    elif action == "take":
        print(f"I gave you ${money}")
        money = 0
display_machine()
write_action()
display_machine()
