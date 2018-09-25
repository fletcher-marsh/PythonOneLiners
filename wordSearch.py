'''
Word Search: given a 2-d list of characters, return 
	(word, (row, col), direction)
as the result of finding the given word in the grid.
Otherwise, return
	None

Source: Fletcher
Characters: 719
'''
from functools import reduce

wordSearch = lambda board, word: reduce(lambda a, b: a if a != None else b, reduce(lambda c, d: c if any(c) else d, [[reduce(lambda x, y: x if x != None else y, reduce(lambda x, y: x if any(x) else y, [[None if (dcol == 0 and drow == 0) else None if (True in [True if (((row + i*drow) < 0) or ((row + i*drow) >= len(board)) or ((col + i*dcol) < 0) or ((col + i*dcol) >= len(board[0])) or (board[(row + i*drow)][(col + i*dcol)] != word[i])) else False for i in range(len(word))]) else (word, (row, col), [["up-left","up","up-right"],["left","","right"],["down-left","down","down-right"]][drow+1][dcol+1]) for dcol in [-1, 0, 1]] for drow in [-1, 0, 1]])) for col in range(len(board[0]))] for row in range(len(board))]))

def testWordSearch():
    board = [ [ 'd', 'o', 'g' ],
              [ 't', 'a', 'c' ],
              [ 'o', 'a', 't' ],
              [ 'u', 'r', 'k' ],
            ]
    print(wordSearch(board, "dog")) # ('dog', (0, 0), 'right')
    print(wordSearch(board, "cat")) # ('cat', (1, 2), 'left')
    print(wordSearch(board, "tad")) # ('tad', (2, 2), 'up-left')
    print(wordSearch(board, "cow")) # None

testWordSearch()