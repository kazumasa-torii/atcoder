import sys
import collections
input = sys.stdin.readline
size, limit = map(int, input().split())
li = [list(input().split())[0] for _ in range(size)]
def judge(bit):
    tmp = str()
    ans = 0
    for i in range(size):
        if bit & (1 << i):
            tmp += li[i]
    tmp = collections.Counter(list(tmp))
    for i, v in enumerate(tmp):
        if tmp[v] != limit:
            continue
        ans += 1
    return ans

A = 0
for bit in range(1 << size):
    A = max(A, judge(bit))
print(A)
