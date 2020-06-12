import random

print("""H A N G M A N""")


class Game:
    def play(self, word):
        hint = "".join(list("-" * len(word)))
        tries = 8
        while tries > 0:
            print(f"\n{hint}")
            if "-" not in list(hint):
                return "You guessed the word!\nYou survived!"
            guess = input("Input a letter: ")
            loc = [pos for pos, char in enumerate(word) if char == guess]
            if not loc:
                tries -= 1
                print("No such letter in the word")
            elif guess in list(hint):
                tries -= 1
                print("No improvements")
            else:
                hint = list(hint)
                for n in loc:
                    hint[n] = guess
                hint = "".join(hint)

        return "You are hanged!"

    def choose_word(self, words=['python', 'java', 'kotlin', 'javascript']):
        return random.choice(words)


game = Game()
print(game.play(word=game.choose_word()))
