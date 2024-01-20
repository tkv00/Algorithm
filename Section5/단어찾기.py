import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 5/8. 단어찾기/in5.txt")
N=int(input())
hash={}
for i in range(N):
    word=input()
    hash[word]=1
for i in range(N-1):
    word=input()
    hash[word]=0
print(hash)

for word in hash:
    if hash[word]==1:
        print(word)