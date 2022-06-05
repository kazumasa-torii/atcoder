import sys
input = sys.stdin.readline
A, B = map(int, input().split())
# tmp = A
# for i in range(A, B):
#     tmp = tmp ^ (i+1)

# print(tmp)
print(bin(A), bin(B))
