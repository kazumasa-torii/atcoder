import sys

input = sys.stdin.readline
S = input().split()
S = list(S[0])
o = []
x = []
for i, v in enumerate(S):
    if v == 'o':
        o.append(str(i))
    elif v == 'x':
        x.append(str(i))

def judge(s):
    for i in o:
        if i not in s:
            return False
        
    for i in x:
        if i in s:
            return False
    return True


ans = 0

for i in range(10000):
    s = str(i).zfill(4)
    if judge(s):
        ans += 1

print(ans)
