import random
print("H A N G M A N")
list = ["python", "java", "kotlin", "javascript"]
random_word = list[random.randint(1,4)-1]
tries = 8
hint = ["-"] * len(random_word)
while tries > 0:
    print()
    print("".join(hint))
    guess = input("Input a letter:")
    if guess in random_word:
        for i in range(len(random_word)):
            if random_word[i] == guess:
                hint[i] = guess
    else:
        print("No such letter in the word\n")
    tries = tries - 1
print("\nThanks for playing!\nWe'll see how well you did in the next stage")