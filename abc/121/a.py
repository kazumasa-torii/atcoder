import sys
input = sys.stdin.readline
A, B = map(int,input().split())
a, b = map(int,input().split())
ans_a = A - a
ans_b = B - b
print(ans_a * ans_b)
