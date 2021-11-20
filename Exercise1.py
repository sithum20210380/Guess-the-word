import random
secret_word = ['westminister','cricket','covid']
word = random.choice(secret_word)
print(word)

print("Let's play Guess the word")
print("You have 6 turns to guess the word!")

guesses=''
turns=6
while turns > 0:
    guess = input("\nguess a character:")
    guess = guess.lower()
    guesses += guess
    missed=0
    for char in word:
        if char in guesses:
            print(char,'\t',end="")
        else:
            print("_",'\t',end="")
            missed+=1
    if missed == 0:
        print("")
        print("end of game")
        break


    if guess not in word:

        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print("End of Game")
            print("The word is:", word)