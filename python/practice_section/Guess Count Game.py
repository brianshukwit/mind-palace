# Guess Count Game
# 9/18/2020 / Brian Shukwit

secret_word = "word"
guess = ""
guessCount = 0
guessLimit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guessCount < guessLimit:
        guess = input("Enter secret word: ")
        guessCount += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of guesses, bruh!")
else:
    print("You win!")
