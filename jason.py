fileName = input("Enter File name: ") #ask for a file (including directory)
def fileOpen(file): #opens and reads a file
    openedFile = open(file)
    readFile = openedFile.read()
    return(readFile)

def textFreq(text): #splits text into words in a list, then lists their frequencies
    splitText = text.split()
    freqText = set(splitText)
    ffreqText = []
    for i in freqText:
        print("Word: ",i," | Frequency: ", splitText.count(i))
  
temp = fileOpen(fileName) #runs fileOpen
textFreq(temp) #runs textFreq