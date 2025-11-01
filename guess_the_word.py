#guess_the_word.py
import random
def wordList():
    word_list = ["HELLO","WORD","BEAN","ROUGH","TYPO","CHILI"]
    return word_list
def getWord(wordList):
    word = random.choice(wordList)
    return word
def letterChecker(guess,count,word):
    if(guess.upper() == word[count]):
        return True
    else:
        return False
def gameLoop():
    is_running = True
    user_guess =""
    count = 0
    word_list = wordList()
    word = getWord(word_list)
    while is_running and user_guess.upper() != word:
        current_input = str(input("Please enter your letter guess: "))
        if(letterChecker(current_input, count,word)):
            print("That letter was correct! Good job! Your current guess looks like: ")
            count = count +1
            user_guess += current_input
            print(user_guess)
        else:
            print("I'm sorry, your guess does not match the expected letter. Please try again")
def main():
    print("Welcome to word guesser")
    print("The goal of the game is to enter letter by letter the word we chose")
    gameLoop()
    print("You completed the game! Good job!")

if __name__ == '__main__':
    main()
