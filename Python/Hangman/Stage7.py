import random

print("""H A N G M A N""")


class Game:
    def play(self, word):
        hint = "".join(list("-" * len(word)))
        tries = 8
        guessed = set()
        while tries > 0:
            print(f"\n{hint}")
            if "-" not in list(hint):
                return "You guessed the word!\nYou survived!"
            guess = input("Input a letter: ")
            if len(guess) != 1:
                print("You should input a single letter")
                continue
            if not (guess.isascii() and guess.islower()):
                print("It is not an ASCII lowercase letter")
                continue
            if guess in guessed:
                print("You already typed this letter")
            elif guess not in word:
                tries -= 1
                print("No such letter in the word")
            else:
                hint = list(hint)
                for i in range(len(hint)):
                    if hint[i] == guess:
                        hint[i] = guess
                hint = "".join(hint)
            guessed.add(guess)
        return "You are hanged!"

    def choose_word(self, words=['python', 'java', 'kotlin', 'javascript']):
        return random.choice(words)


game = Game()
print(game.play(word=game.choose_word()))
