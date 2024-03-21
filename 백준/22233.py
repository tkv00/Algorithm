# 가희와 키워드
import sys

key_n, post_n = map(int, sys.stdin.readline().split(' '))

memo = {}
answer = 0

for _ in range(key_n):
    memo[sys.stdin.readline().rstrip()] = 1
    answer += 1

for _ in range(post_n):
    post = list(sys.stdin.readline().rstrip().split(','))
    for i in post:
        if i in memo.keys():
            if memo[i] == 1:
                memo[i] = 0
                answer -= 1
    print(answer)