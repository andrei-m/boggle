#!/usr/bin/python
import re

class TrieNode:
    """A trie node representing a word or word prefix. To be Boggle-friendly,
       'q's in this tree represent 'qu'"""
    def __init__(self, parent, value):
        self.parent = parent
        self.children = [None] * 26
        self.isWord = False
        if parent is not None:
            parent.children[ord(value) - 97] = self

def MakeTrie(dictfile):
    """ Construct a trie from the given dictionary, excluding words
        containing a 'q' not followed by a 'u'"""
    dict = open(dictfile)
    root = TrieNode(None, '')
    regex = re.compile('.*q[^u].*')
    for word in dict:
        word = word.rstrip()
        if len(word) >= 3 and not regex.match(word):
            # Let 'q' represent 'qu'
            word = word.replace('qu', 'q')
            curNode = root
            for letter in word.lower():
                if 97 <= ord(letter) < 123:
                    nextNode = curNode.children[ord(letter) - 97]
                    if nextNode is None:
                        nextNode = TrieNode(curNode, letter)
                    curNode = nextNode
            curNode.isWord = True
    return root
