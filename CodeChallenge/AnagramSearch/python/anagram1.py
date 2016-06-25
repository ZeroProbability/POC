# Given a words.txt file containing a newline-delimited list of dictionary
# words, please implement the Anagrams class so that the get_anagrams() method
# returns all anagrams for a given word from words.txt.
#
# Bonus requirements:
#   - Optimise the code for fast retrieval
#   - Write more tests
#   - Thread safe implementation

import unittest
import itertools

class WordNode(object):
    def __init__(self, node_char):
        self._is_a_word = False
        self._node_char = node_char
        self._children = {}

    def insert_word(self, word):
        first_char = word[0]
        rest = word[1:]
        #print "{} inserting {}".format(first_char, rest)

        if rest == "":
            new_child = WordNode(first_char)
            self._children[first_char] = new_child
            #print "setting {} is word".format(new_child._node_char)
            new_child._is_a_word = True
            return word
        
        if self._children.get(first_char) is None:
            new_child = WordNode(first_char)
            self._children[first_char] = new_child
            new_child.insert_word(rest)
        else:
            self._children.get(first_char).insert_word(rest)

    def get(self, child_char):
        return self._children.get(child_char)

class WordTree(object):
    def __init__(self, words_iter):
        self.__top_node = WordNode("")
        for word in words_iter:
            self.__top_node.insert_word(word)

    def is_word_present(self, word):
        chars = list(word.lower())
        if len(chars) == 0:
            return False
        current_search_head = self.__top_node

        while True: 
            c = chars.pop(0)
            #print "searching {}".format(c)
            next_head = current_search_head.get(c)
            if next_head == None:
                return False

            if len(chars) == 0:
                #print "{} is {}".format(next_head._node_char, next_head._is_a_word)
                return next_head._is_a_word


            current_search_head = next_head


class Anagrams(object):

    def __init__(self):
        self.words = open('words.txt').readlines()
        self._word_tree = WordTree((w.rstrip().lower() for w in self.words))

    def get_anagrams(self, word):
        word_len = len(word)
        ret_list = []
        for ana_word in (''.join(w) for w in itertools.permutations(word.lower())):
            if self._word_tree.is_word_present(ana_word):
                ret_list.append(ana_word)

        return sorted(ret_list)

class TestWordTree(unittest.TestCase):

    def test_adding_a_word(self):
        tree = WordTree(["some"])
        self.assertFalse(tree.is_word_present("other"))
        self.assertTrue(tree.is_word_present("some"))

        tree = WordTree(["some", "someother"])
        self.assertFalse(tree.is_word_present("other"))
        self.assertTrue(tree.is_word_present("some"))
        self.assertFalse(tree.is_word_present("someo"))
        self.assertTrue(tree.is_word_present("someother"))
        self.assertFalse(tree.is_word_present("someother1"))
        self.assertFalse(tree.is_word_present("somex"))

        tree = WordTree(["eat", "tea"])
        self.assertTrue(tree.is_word_present("eat"))
        self.assertTrue(tree.is_word_present("EAT"))
        self.assertTrue(tree.is_word_present("tea"))
        self.assertFalse(tree.is_word_present("ate"))
        self.assertFalse(tree.is_word_present(""))

        
class TestAnagrams(unittest.TestCase):

    def test_anagrams(self):
        anagrams = Anagrams()

        self.assertEquals(anagrams.get_anagrams('eat'), ['ate', 'eat', 'tea'])
        self.assertEquals(anagrams.get_anagrams('EAT'), ['ate', 'eat', 'tea'])
        self.assertEquals(anagrams.get_anagrams('pears'), ['pares', 'parse', 'pears', 'rapes', 'reaps', 'spare', 'spear'])

if __name__ == '__main__':
    unittest.main()
