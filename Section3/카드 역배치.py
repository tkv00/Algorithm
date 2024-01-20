import sys
sys.stdin=open("/Users/kimdoyeon/Downloads/pythonalgorithm_formac/섹션 3/3. 카드 역배치/in1.txt","rt")

def list_print(x):
    for num in x:
        print(num, end=' ')

def reverse_list(x, a, b):
     for i in range((b - a + 1) // 2):
            left = a - 1 + i
            right = b - 1 - i
            x[left], x[right] = x[right], x[left]

num = []
for i in range(20):
    num.append(i + 1)

for i in range(10):
    n, m = map(int, input().split())
    reverse_list(num, n, m)

list_print(num)
