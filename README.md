boggle
======
A boggle solver based on [Adam Rosenfield](http://stackoverflow.com/users/9530/adam-rosenfield)'s Stack Overflow [answer](http://stackoverflow.com/questions/746082/how-to-find-list-of-possible-words-from-a-letter-matrix-boggle-solver#746102).
This version contains these differences:
* 'Qu' is represented by one element in the matrix
* The same matrix element cannot be used more than once for a single word
* Words shorter than 3 characters are ineligible

## Usage ##
```
./boggle.py board.txt
```
'board.txt' represents the board, e.g.:
```
zrgr
sykp
yewa
tern
```
Remember: 'q' in this file corresponds to the 'Qu' tile.
