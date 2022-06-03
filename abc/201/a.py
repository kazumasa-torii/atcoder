"""
簡単のifelse
"""
import sys
input = sys.stdin.readline
li = list(map(int, input().split()))
li = sorted(li)
ans_1 = li[1] - li[0]
ans_2 = li[2] - li[1]
print('Yes' if ans_1 == ans_2 else 'No')
