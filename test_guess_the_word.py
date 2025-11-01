#test_guess_the_word.py
#imports the unittest to allow for testing the program
import unittest
#Gets the necessary functions from the main program that will be tested
from guess_the_word import wordList
from guess_the_word import getWord
from guess_the_word import letterChecker
#Generates the list and gets a word from the list
word_list = wordList()
word = getWord(word_list)
#Test class information for the game
class TestGame(unittest.TestCase):
    #Checks if the word is in the word list
    def test_wordInList(self):
        self.assertTrue(word in word_list)
    #Checks if the letter "A" is at the position of 0 for the word (SHOULD ALWAYS BE FALSE NO WORD STARTS WITH A INTENTIONAL FAILURE)
    def test_checkLetter(self):
        self.assertTrue(letterChecker("A",0, word))
    #Checks if the letter at the start of the word matches (SHOULD ALWAYS BE TRUE AS WE ARE USING A DUPLICATE VALUE IF FALSE CHECK LETTER CHECKER FUNCTION IN MAIN FILE)
    def test_checkInput(self):
        self.assertTrue(letterChecker(word[0],0,word[0]))
#Calls the unittest.main() function to allow for testing using pytest or by running this file in the IDLE.
if __name__ == '__main__':
    unittest.main()
