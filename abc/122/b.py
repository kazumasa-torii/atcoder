import sys
input = sys.stdin.readline
S = list(map(str, input().split()))
S = list(S[0])
str_set = {'A', 'C', 'G', 'T'}
ans = 0
for i in range(len(S)):
    if not(set(S[i]) & str_set):
        continue
    tmp = 1
    for j in range(i+1, len(S)):
        if j > len(S):
            continue
        if not(set(S[j]) & str_set):
            break
        tmp += 1
    ans = max(ans, tmp)
print(ans)
