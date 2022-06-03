S = input()
T = input()
slen = len(S)
tlen = len(T)
dp = [[0] * (tlen+1) for _ in range((slen+1))]
ans = str()

# 一致する文字列の最長を求める
for i in range(slen):
    for j in range(tlen):
        r = max(dp[i+1][j], dp[i][j+1])
        if S[i] == T[j]:
            r = dp[i][j] + 1
        dp[i+1][j+1] = r

# 文字列復活
length = dp[slen][tlen]
slen -= 1
tlen -= 1
ans = str()
while length > 0:
    if S[slen] == T[tlen]:
        ans = S[slen] + ans
        slen -= 1
        tlen -= 1
        length -= 1
    elif dp[slen][tlen] == dp[slen-1][tlen]:
        slen -= 1
    else:
        tlen -= 1
print(ans)
