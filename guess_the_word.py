import random
word_list = ["HELLO","WORD","BEAN","ROUGH","TYPO","CHILI"]
word = random.choice(word_list)
user_guess =""
count = 0
print("Welcome to work guesser")
print("The goal of the game is to enter letter by letter the word we chose")
while user_guess.upper() != word:
    current_input = str(input("Please enter your letter guess: "))
    if(current_input.upper() == word[count]):
        print("That letter was correct! Good job! Your current guess looks like: ")
        count = count +1
        user_guess += current_input
        print(user_guess)
    else:
        print("I'm sorry, your guess does not match the expected letter. Please try again")

print("You completed the game! Good job!")
