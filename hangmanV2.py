def internetRead(internetUrl): #takes an url, returns a text block (50,000 bytes) of the html
    from urllib import request
    internetFile = request.urlopen(internetUrl)
    file = internetFile.read(50000)
    return (file)

def splitParse(toParse): #takes a file, splits it into a list of words, removes "words" that include non-letter characters, returns the list in all lowercase
    split = toParse.split()
    parsed = []
    for words in split:
        if words.isalpha() == True and len(words) >= 4:
            lwords = words.lower()
            parsed.append(lwords)
    i = 0
    parsed2 = []
    while i < len(parsed):
        parsed2.append(parsed[i].decode('utf-8'))
        i += 1
    return (parsed2)

def aiSelectBank(wordBankURL):  #combines internetRead and splitParse
    x = internetRead(wordBankURL)
    y = splitParse(x)
    return (y)

def writeSlowly(text): #prints characters "slowly" to appear human-like   
    import random, time, sys 
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(random.random())

def aiSelectSkill0(wordBank): #selects a large word from the bank, therefore being relatively easy
    import random
    wordBankLoc = aiSelectBank(wordBank)
    rand0 = random.randint(0,25)
    sortedWordBank = sorted(wordBankLoc, key=len, reverse=True)
    return (sortedWordBank[rand0])

def aiSelectSkill1(wordBank): #uses a normal distribution, rounding to nearest integer, to choose a moderately difficult (by length) word - could be used to make a variety of difficulties
    import random, numpy
    wordBankLoc = aiSelectBank(wordBank)
    sortedWordBank = sorted(wordBankLoc, key=len, reverse=True)
    rand1 = -1
    while rand1 > 1 or rand1 < 0:
        rand1 = round(numpy.random.normal(.5,.5)*len(wordBankLoc))
    return (sortedWordBank[rand1])

def aiSelectSkill2(wordBank): #returns any random word from the bank
    import random
    wordBankLoc = aiSelectBank(wordBank)
    return(random.choice(wordBankLoc))

def aiSelectSkill3(wordBank): #returns a small word from the bank, therefore being relatively difficult
    import random
    wordBankLoc = aiSelectBank(wordBank)
    rand3 = random.randint(0,25)
    sortedWordBank = sorted(wordBankLoc, key=len)
    return(sortedWordBank[rand3])

#dictonary of lowercase characters and their corresponding frequency, as well as lists of 

frequencyChars = {'a':.08167,'b':.01492,'c':0.02782,'d':.04253,'e':.12702,'f':.02228,'g':.02015,'h':.06094,'i':.06966,'j':.00153,'k':.00772,'l':.04025,'m':.02406,'n':.06749,'o':.07507,'p':.01929,'q':.00095,'r':.05987,'s':.06327,'t':.09056,'u':.02758,'v':.00978,'w':.02360,'x':.00150,'y':.01974,'z':.00074}
sortedChars = sorted(frequencyChars,key=frequencyChars.__getitem__,reverse=True)
sortedValues = sorted(frequencyChars.values(),reverse=True)

def aiGuessSkill0(guessedLetters): #picks the character with the lowest frequency (deliberately bad algorithm)
    i = -1
    guess = '.'
    while guess in guessedLetters or guess == '.':
        guess = sortedChars[i]
        i -= 1
    return(guess)

def aiGuessSkill1(guessedLetters): #guesses a random character
    import random, string
    guess = '.'
    while guess in guessedLetters or guess == '.':
        guess = random.choice(string.ascii_lowercase)
    return(guess)

def aiGuessSkill2(guessedLetters): #guesses a character based on a normal distribution and the frequency (could be skewed to increase or decrease difficulty)
    import numpy
    guess = '.'
    rand = -1
    while guess in guessedLetters or guess == '.' or rand > len(sortedChars) or rand < 0:
        rand = round(numpy.random.normal(.5,.5)*len(sortedChars))
        if rand < len(sortedChars) and rand > 0:
            guess = sortedChars[rand]
    return(guess)

def aiGuessSkill3(guessedLetters): #guesses a character based on their frequencies (choosing the most frequent charcter not yet selected)
    i = 0
    guess = '.'
    while guess in guessedLetters or guess == '.':
        guess = sortedChars[i]
        i += 1
    return(guess)

def aiGuessSkill(skillLevel,guessedLetters): #combines guessSkill functions to be easily callable
    if skillLevel == 0:
        return(aiGuessSkill0(guessedLetters))
    elif skillLevel == 1:
        return(aiGuessSkill1(guessedLetters))
    elif skillLevel == 2:
        return(aiGuessSkill2(guessedLetters))
    elif skillLevel == 3:
        return(aiGuessSkill3(guessedLetters))
    else:
        print("guessSkill error")
    
def aiSelectSkill(skillLevel,wordBank): #combines selectSkill functions to be easily callable
    if skillLevel == 0:
        return(aiSelectSkill0(wordBank))
    elif skillLevel == 1:
        return(aiSelectSkill1(wordBank))
    elif skillLevel == 2:
        return(aiSelectSkill2(wordBank))
    elif skillLevel == 3:
        return(aiSelectSkill3(wordBank))
    else:
        print("selectSkill error")
        
def hangman(numPlayers, playerControlled = 0, aiOneSkill = 0, aiTwoSkill = 0, wordBank = '', playerChosenWord = ''):
    import time
    guessed = False
    guessedLetters = []
    wrongGuesses = 0
    if numPlayers == 0 or (numPlayers == 1 and playerControlled == 2):
        word = aiSelectSkill(aiOneSkill,wordBank)
    elif numPlayers == 2 or (numPlayers == 1 and playerControlled == 1):
        word = playerChosenWord
    else:
        print("Word Selection Error")
    if numPlayers == 0:
        writeSlowly(word)
    wordShown = list("-"*len(word))
    while guessed != True and wrongGuesses < 15:
        print(''.join(wordShown))
        print("Guessed letters:", guessedLetters)
        if numPlayers == 0 or (numPlayers == 1 and playerControlled == 1):
            guess = aiGuessSkill(aiTwoSkill,guessedLetters)
            print(guess)
            time.sleep(1)
        elif numPlayers == 2 or (numPlayers == 1 and playerControlled == 2):
            guess = input("Player 2, enter a letter: ")
        else:
            print("Character guess error")
        while guess in guessedLetters or len(guess) != 1:
            print("You've already picked this letter or it's not one letter!")
            guess = input("Pick another letter: ")
        guessedLetters.append(guess)
        if guess in word:
            print("Correct!")
            i = 0
            while i < len(word):
                if guess == word[i]:
                    wordShown[i] = guess
                    if not "-" in wordShown:
                        print("Player (or CPU) 2 Wins!")
                        guessed = True
                i += 1
        else:
            print("Incorrect")
            wrongGuesses += 1
            if wrongGuesses == 15:
                print("Player (or CPU) 1 Wins!")
                print(word)

def playHangman():
    numberofPlayers = -1
    while numberofPlayers not in range(0,3):
        numberOfPlayers = int(input("Enter number of players controlled (0, 1 or 2): "))
        if numberOfPlayers == 2:
            chosenWord = str.lower(input("Player 1, choose a word: "))
            hangman(numberOfPlayers,playerChosenWord = chosenWord)
        elif numberOfPlayers == 1:
            playerCont = -1
            aiSkill = -1
            while playerCont not in range(1,3) or aiSkill not in range(0,4):
                playerCont = int(input("Enter which player you'd like to play as (1 = selecting word, 2 = guessing word): "))
                aiSkill = int(input("Enter the desired skill level of the CPU (0-3): "))
                if playerCont == 1 and aiSkill in range(0,4):
                    chosenWord = str.lower(input("Choose a word for the CPU to guess: "))
                    hangman(1,1,0,aiSkill,playerChosenWord = chosenWord)
                if playerCont == 2 and aiSkill in range(0,4):
                    wordBankURL = input("Enter a url to be used as a word bank for the CPU (including https://): ")
                    hangman(1,2,aiSkill,0,wordBank = wordBankURL)
        elif numberOfPlayers == 0:
            aiSkillOne = -1
            aiSkillTwo = -1
            while aiSkillOne not in range (0,4) or aiSkillTwo not in range(0,4):
                wordBankURL = input("Enter a url to be used as a word bank for the CPU (including https://): ")
                aiSkillOne = int(input("Enter a skill level for the word selecting CPU (0-3): "))
                aiSkillTwo = int(input("Enter a skill level for the word guessing CPU (0-3): "))
                hangman(0,0,aiSkillOne,aiSkillTwo,wordBank = wordBankURL)
                if aiSkillOne not in range (0,4) or aiSkillTwo not in range(0,4):
                    print("Please select valid skill levels")
        else:
            print("Not a valid number of players")
                

def main():
    playHangman()

if __name__=="__main__":
    main()

