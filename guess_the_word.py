#guess_the_word.py
#DOM2136411 CIS256 EX4
#Imports random function to call the random word choice
import random
#Creates the word list
def wordList():
    word_list = ["HELLO","WORD","BEAN","ROUGH","TYPO","CHILI"]
    #returns the word list as an output
    return word_list
#Gets the word from the word list
def getWord(wordList):
    word = random.choice(wordList)
    #returns the word to be guessed
    return word
#Checks the user input against the letter of the word at the current index location
def letterChecker(guess,count,word):
    #Sets the letter guessed to be upper if needed and returns true if matching else returns false
    if(guess.upper() == word[count]):
        return True
    else:
        return False
#Defines the main loop information for the file
def gameLoop():
    #Variable to store the user guess
    user_guess =""
    #Index variable
    count = 0
    #Gets the word list
    word_list = wordList()
    #Gets the word from the word list
    word = getWord(word_list)
    #loop to ensure that word guess can continue over entire word
    while user_guess.upper() != word:
        #Gets user input
        current_input = str(input("Please enter your letter guess: "))
        #Calls the letter checker to check the user input against the current letter of the word
        if(letterChecker(current_input, count,word)):
            #output to user if letter correct
            print("That letter was correct! Good job! Your current guess looks like: ")
            #increases index location
            count = count +1
            #updates user guess information string
            user_guess += current_input
            #prints the currently guessed letters for the user
            print(user_guess)
        #prints a negative message for user when input does not match the current letter
        else:
            print("I'm sorry, your guess does not match the expected letter. Please try again")
#Main loop
def main():
    #Opening headers
    print("Welcome to word guesser")
    print("The goal of the game is to enter letter by letter the word we chose")
    #Calls the game loop
    gameLoop()
    #Prints when game is over
    print("You completed the game! Good job!")
#Allows for unit testing as when in test __name__ does not equal __main__ so tests can run without being stuck by main loop.
if __name__ == '__main__':
    #Starts the main loop
    main()
