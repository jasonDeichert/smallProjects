def hangman():
    word = input("Player 1, enter a word: ")
    guessed = False
    guessedLetters = []
    wordShown = list("-"*len(word))
    wrongGuesses = 0
    while guessed != True and wrongGuesses < 10:
        print(''.join(wordShown))
        print("Guessed letters:", guessedLetters)
        guess = input("Player 2, enter a letter: ")
        while guess in guessedLetters or len(guess) != 1:
            print("You've already picked this letter or it's more than one letter!")
            guess = input("Pick another letter: ")
        guessedLetters.append(guess)
        if guess in word:
            print("Correct!")
            i = 0
            while i < len(word):
                if guess == word[i]:
                    wordShown[i] = guess
                    if not "-" in wordShown:
                        print("You Win!")
                        guessed = True
                i += 1
        else:
            print("Incorrect")
            wrongGuesses += 1
            if wrongGuesses == 10:
                print("You lose!")

def main():
    hangman()

if __name__=="__main__":
    main()
    


        


    

