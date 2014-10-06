# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

MAX_GUESS = 10

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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
    count = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            count += 1
    if count == len(secretWord):
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    result = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            result += letter
        else:
            result += '_ '
    return result



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    resultstr = ''
    for letter in string.ascii_lowercase:
        if letter in lettersGuessed:
            pass
        else:
            resultstr += letter
    return resultstr
    

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
    # Total number of guesses available to user for a word is 10
    numberOfGuesses = MAX_GUESS
    # An empty list to which user's correct guesses are added
    lettersGuessed = {}
    # Welcome message
    print 'Welcome to Hangman..! The word guessing game.'
    print 'The length of the secret word is %s.' %(str(len(secretWord)))
    print 'Guess the word.'
    for i in range(len(secretWord)):
        print '_',
    print '\n'
    
    while True:
        
        if not isWordGuessed(secretWord , lettersGuessed):
            # Word not guessed
            if numberOfGuesses == 0:
                # all guesses exhausted
                print 'Sorry , YOU LOST. :(  \nThe word is %s' %(secretWord)
                break
            else:
                # Displaying number of guesses left and available letters
                print 'You have %s guesses left.' %(str(numberOfGuesses))
                print 'Available letters : %s' %(getAvailableLetters(lettersGuessed))
                # Taking user input
                guessedLetter = raw_input('\nPlease enter a letter: ')

                if guessedLetter in lettersGuessed:
                    # If already guessed letter is entered
                    print 'Already guessed this letter %s' %(getGuessedWord(secretWord , lettersGuessed))
                else:
                    # New letter is guessed by the user
                    lettersGuessed[guessedLetter] = True
                    # Wrong guess
                    if guessedLetter not in secretWord:
                        print 'Letter not in Secret word : %s' %(getGuessedWord(secretWord , lettersGuessed))
                        numberOfGuesses -= 1
                    else:
                        # Right guess
                        print 'Good guess: %s' %(getGuessedWord(secretWord , lettersGuessed))

        else:
            # Complete word is guessed
            print 'Congratulations , YOU WON. :) '
            break






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
