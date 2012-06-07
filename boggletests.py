#!/usr/bin/python
import unittest
import boggle

class TrieParseTests(unittest.TestCase):
    """Tests for parsing a dictionary into a trie"""

    def setUp(self):
        self.root = boggle.MakeTrie('testdict.txt')

    def testWord(self):
        """Test the basic case for 'one'"""
        currentNode = self.root.children[ord('o') - 97]
        self.assertFalse(currentNode.isWord)
        currentNode = currentNode.children[ord('n') - 97]
        self.assertFalse(currentNode.isWord)
        currentNode = currentNode.children[ord('e') - 97]
        self.assertTrue(currentNode.isWord)

    def testIsWord(self):
        """Test the 'isWord' flag for a non-leaf node"""
        currentNode = self.root.children[ord('a') - 97]
        self.assertFalse(currentNode.isWord)
        currentNode = currentNode.children[ord('d') - 97]
        self.assertFalse(currentNode.isWord)
        currentNode = currentNode.children[ord('d') - 97]
        self.assertTrue(currentNode.isWord)
        currentNode = currentNode.children[ord('e') - 97]
        self.assertFalse(currentNode.isWord)
        currentNode = currentNode.children[ord('r') - 97]
        self.assertTrue(currentNode.isWord)


    def testExcludeShortWord(self):
        """Assert that words shorter than 3 chars are excluded"""
        # 'pi' is excluded; there is no other word beginning with 'p'
        self.assertTrue(self.root.children[ord('p') - 97] is None)

    def testExcludeQnotU(self):
        """Assert that the word with a q lacking a following u is excluded"""
        self.assertTrue(self.root.children[ord('s') - 97] is None)

if __name__ == '__main__':
    unittest.main()
