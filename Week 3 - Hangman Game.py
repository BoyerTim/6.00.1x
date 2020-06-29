###Problem Set 3###

# Hangman game
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for letter in secretWord: #iterate over letters in secretWord
        if letter not in lettersGuessed: #check if each letter from secretWord is NOT in the list of letters guessed so far 
            return False #if one of the letters from the secretWord isn't in the guessed letters, return False and exit the function 
    return True # if all the letters in secretWord are in the Guessed list, great, you have the word


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    word = ""
    for letter in secretWord: #loop over secret word
        if letter in lettersGuessed: #if the letter has been guessed, add to var "word"
            word += letter
        else:                       #if letter not in guessed list
            word += "_ "             #print _
    return word

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    #string is immutable so use list to remove letters as they are guess
    remaining_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in lettersGuessed:
        if letter in remaining_letters:
            remaining_letters.remove(letter) #if the letter is in lettersGuessed, remove from reamining_letters
    k = ""
    k = k.join(remaining_letters)
    return k  #returns string of remaining letters 
    
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    guessesLeft = 8
    lettersGuessed = []
    
    while guessesLeft > 0: #keep looping while within valid number of guesses
        print("-----------")
        print("You have", guessesLeft, "guesses left.")
        print("Available letters:", getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ").lower()                                        #need new line?
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))

        elif guess in getAvailableLetters(lettersGuessed):
            lettersGuessed += guess    
            if guess in secretWord:
                print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
                if isWordGuessed(secretWord, lettersGuessed) == True: #Game won
                    print("-----------")
                    print("Congratulations, you won!")
                    return
            else:    
                print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
                guessesLeft -= 1 #only lose guess when incorrect

    print("-----------")
    print("Sorry, you ran out of guesses. The word was", secretWord + ".")


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
#secretWord = "test"
hangman(secretWord)
