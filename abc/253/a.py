import sys
input = sys.stdin.readline
a, b, c= list(map(int, input().split()))
ls = [a, b, c]
ls.sort()
print('Yes' if ls[1] == b else 'No')
