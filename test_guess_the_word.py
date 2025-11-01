#test_guess_the_word.py
import unittest
from guess_the_word import wordList
from guess_the_word import getWord
from guess_the_word import letterChecker
word_list = wordList()
word = getWord(word_list)
class TestGame(unittest.TestCase):
    def test_wordInList(self):
        self.assertTrue(word in word_list)
    def test_checkLetter(self):
        self.assertTrue(letterChecker("A",0, word))
    def test_checkInput(self):
        self.assertTrue(letterChecker(word[0],0,word[0]))
    
if __name__ == '__main__':
    unittest.main()
