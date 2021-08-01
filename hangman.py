import random

with open('test.txt') as f:
    words = list(f)
word = (random.choice(words).strip())


def gen_dashes(n):
    dash = ""
    while n > 0:
        dash += "-"
        n = n-1
    return dash


dashes = gen_dashes(len(word))


def update_dash(wrd, dsh, guess):
    if (wrd == "") and (dsh == ""):
        return ""
    elif guess == list(wrd)[0]:
        return guess+update_dash(wrd[1:], dsh[1:], guess)
    else:
        return list(dsh)[0]+update_dash(wrd[1:], dsh[1:], guess)


def hg(wrd, dsh, y):
    print("")
    guess = input("Enter your guess: ")
    while y >= 0:
        if not(guess.isalpha()):
            print("Invalid Input")
            print("Your current word after guessing is",
                  update_dash(wrd, dsh, guess))
            print("Number of wrong guess left:", y)
            return hg(wrd, update_dash(wrd, dsh, guess), y)
        elif wrd == update_dash(wrd, dsh, guess):
            print("You won the game!!!",
                  "\nThe secret word you guessed was", "'", wrd, "' .")
            break
        elif guess in wrd:
            print("Your guess lies in the secret word")
            print("Your current word after guessing is",
                  update_dash(wrd, dsh, guess))
            print("Number of wrong guess left:", y)
            return hg(wrd, update_dash(wrd, dsh, guess), y)
        elif not(guess in wrd):
            print("Your guess does not lie in the secret word")
            print("Number of wrong guesses left:", y-1)
            return hg(wrd, update_dash(wrd, dsh, guess), y-1)

    if wrd == update_dash(wrd, dsh, guess):
        return None
    print("Maximum number of wrong guesses exceeded!!!")
    print("You lose :(")
    print("The word you could not guess was", "'", wrd, "' .")


def hangman():
    print("Number of letters in the word to be guessed:", len(word))
    print("If the number of wrong guesses left is -1 that means you have lost the game.")
    return hg(word, dashes, 6)


hangman()
