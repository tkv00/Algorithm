import sys

def solution() :
    n, m = map(int, sys.stdin.readline().split())
    board = dict()
    for _ in range(n) :
        board[sys.stdin.readline().rstrip()] = 1
        
    res = n
    for _ in range(m) :
        tmp = sorted(sys.stdin.readline().rstrip().split(','))
        
        for t in tmp :
            if t in board.keys() :
                if board[t] == 1 :
                    board[t] -= 1
                    res -= 1
        print(res)
        
solution()