import random
lets_see = ('python', 'java', 'kotlin', 'javascript')
while True:
    action = input('Type "play" to play the game, "exit" to quit:')
    while action not in ['play', 'exit']:
        action = input('Type "play" to play the game, "exit" to quit:')
        
    if action == 'exit':
        break

    random_word = random.choice(lets_see)
    random_word = "javascript"
    list_word = list(random_word)
    set_word = set(random_word)
    print("H A N G M A N\n")
    hidden_word = ['-' for i in random_word]
    print("".join(hidden_word))
    used_letters = set()
    i = 8
    correct = 0
    while i > 0:
        letter = input("Input a letter:")
        if letter in used_letters:
            print("You already typed this letter")
            print()
            print("".join(hidden_word))
            continue
 
        if letter in set_word:
            if letter not in hidden_word:
                k = 0
                for j in list_word:
                    if letter == j:
                        hidden_word[k] = letter
                        if letter not in used_letters:
                            used_letters.add(letter)
                        correct += 1
                    k += 1
        else:
            if len(letter) != 1:
                print("You should input a single letter")
            elif letter.isascii() and not letter.islower():
                print("It is not an ASCII lowercase letter")
            else:
                print("No such letter in the word")
                used_letters.add(letter)
                i -= 1
        if correct == len(random_word):
            print(f"You guessed the word {random_word}!")
            print("You survived!")
            break
        if i == 0:
            print("You are hanged!")
            break
        print()
        print("".join(hidden_word))