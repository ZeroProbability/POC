# Given a words.txt file containing a newline-delimited list of dictionary
# words, please implement the Anagrams class so that the get_anagrams() method
# returns all anagrams for a given word from words.txt.
#
# Bonus requirements:
#   - Optimise the code for fast retrieval
#   - Write more tests
#   - Thread safe implementation

import unittest

class WordNode(object):
    def __init__(self, node_char):
        self._is_a_word = False
        self._node_char = node_char
        self._children = {}

    def insert_word(self, word):
        first_char = word[0]
        rest = word[1:]
        if rest == "":
            self._is_a_word = True
            return word
        

class WordTree(object):
    def __init__(self):
        self._top_node = WordNode("")

    def insert_word(self, word):
        self._top_node.insert_word(word)

    def is_word_present(self, word):
        pass

class Anagrams(object):

    def __init__(self):
        self.words = open('words.txt').readlines()

    def get_anagrams(self, word):
        pass

class TestWordTree(unittest.TestCase):

    def test_adding_a_word(self):
        tree = WordTree()
        tree.insert_word("some")
        self.assertTrue(tree.is_word_present("some"))
        self.assertFalse(tree.is_word_present("other"))

        
#class TestAnagrams(unittest.TestCase):
#
#    def test_anagrams(self):
#        anagrams = Anagrams()
#
#        self.assertEquals(anagrams.get_anagrams('pears'), ['pares', 'parse', 'pears', 'rapes', 'reaps', 'spare', 'spear'])
#        self.assertEquals(anagrams.get_anagrams('eat'), ['ate', 'eat', 'tea'])

if __name__ == '__main__':
    unittest.main()
