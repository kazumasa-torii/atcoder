S = input()
di = {0:0, 1:0}
for i in range(len(S)):
    di[int(S[i])] += 1
ans = min(di[0], di[1]) * 2
print(ans)
