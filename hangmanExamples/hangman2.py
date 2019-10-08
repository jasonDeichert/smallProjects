import random

print("Welcome Player 1")

word = random.choice(["look", "cat", "dog"])

guessed = []
wrong = []
count = 8
while count > 0:

    out = ""
    for letter in word:
        if letter in guessed:
            out = out + letter
        else:
            out = out + "_"

    if out == word:
        break

    print("Guess the word:", "which has", len(word), "Letters", out)
    print(count, "chances left")

    guess = raw_input("What is your guess")

    if guess in guessed or guess in wrong:
        print("Already used", guess)
    elif guess in word:
        print("Correct")
        
        guessed.append(guess)

    else:
        print("Nah")
        count = count - 1
        
        wrong.append(guess)

    

if count:
    print("You guessed", word)
    print("YOU WON!!!")
else:
    print("You lost.The word was", word)
    print("SORRY TRY AGAIN")
