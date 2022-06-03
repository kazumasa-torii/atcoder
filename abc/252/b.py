"""
for一つで考える
"""
import sys
import math
input = sys.stdin.readline
INF = math.inf

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = set(map(int, input().split()))
max_a = max(A)
maxlist = []
for i in range(len(A)):
    if max_a == A[i]:
        maxlist.append(i+1)
print('Yes' if set(maxlist) & B else 'No')
