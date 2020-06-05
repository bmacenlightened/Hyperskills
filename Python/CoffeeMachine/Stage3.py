water = int(input("Write how many ml of water the coffee machine has:\n"))
milk = int(input("Write how many ml of milk the coffee machine has:\n"))
beans = int(input("Write how many grams of coffee beans the coffee machine has:\n"))
cups = int(input("Write how many cups of coffee you will need:\n"))
can_water = water // 200
can_milk = milk // 50
can_beans = beans // 15
if can_water > cups and can_milk > cups and can_beans > cups:
    extra = min(can_water, can_milk, can_beans) - cups
    print(f"Yes, I can make that amount of coffee (and even {extra} more than that)")
elif can_water == cups or can_milk == cups or can_beans == cups:
    print(f"Yes, I can make that amount of coffee")
else:
    can_cups = min(can_water, can_milk, can_beans)
    print(f"No, I can make only {can_cups} cups of coffee")