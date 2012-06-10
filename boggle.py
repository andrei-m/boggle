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
    """Construct a trie from the given dictionary, excluding words
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

def BoggleWords(grid, dict):
    """Find all words from dict that can be constructed from the given grid"""
    rows, cols = len(grid), len(grid[0])
    queue = []
    words = set()
    for y in range(cols):
        for x in range(rows):
            c = grid[y][x]
            node = dict.children[ord(c) - 97]
            if node is not None:
                queue.append((x, y, c, node)) #TODO: a fifth element is needed to keep track of which positions in the grid have been visited to construct the prefix c
    while queue:
        x, y, s, node = queue.pop(0)
        for dx, dy in ((1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)):
            x2, y2 = x + dx, y + dy
            #TODO: this 'if' should check if x2, y2 has been previously visited
            if 0 <= x2 < cols and 0 <= y2 < rows:
                s2 = s + grid[y2][x2]
                node2 = node.children[ord(grid[y2][x2]) - 97]
                if node2 is not None:
                    if node2.isWord:
                        words.add(s2)
                    queue.append((x2, y2, s2, node2))
    return words
                    
