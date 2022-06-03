import sys
input = sys.stdin.readline
ans = 0
N = int(input())

def judge(num):
    index = 0
    for k in range(1, num+1):
        if num % k == 0:
            index += 1
    return index

for i in range(1, N+1):
    if i % 2 == 1:
        if judge(i) == 8:
            ans += 1
print(ans)
