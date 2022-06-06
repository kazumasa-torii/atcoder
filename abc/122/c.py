N, Q = map(int, input().split())
S = input()
sum_str = [0] * N
for i in range(1, len(S)):
    sum_str[i] = sum_str[i-1]
    if S[i-1] == 'A' and S[i] == 'C':
        sum_str[i] += 1

for _ in range(Q):
    x, y = map(int, input().split())
    print(sum_str[y-1] - sum_str[x-1])
