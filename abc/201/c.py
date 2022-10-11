"""

"""
import sys
import time
from io import StringIO
from typing import List


_INPUT = """\
xxxxx?xxxo

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    S = list(input())
    l = len(S)
    ab = []
    no = []
    cnt = 0

    for i in range(l):
        if S[i] == 'o':
            cnt += 1
            ab.append(i)
        if S[i] == 'x':
            no.append(i)
    if cnt > 4:
        print(0)
        return
    ans = 0
    for i in range(10**4):
        tmp = list(str(i).zfill(4))
        flag = True
        for a in ab:
            if str(a) not in tmp:
                flag = False
                break
        for n in no:
            if str(n) in tmp:
                flag = False
        if not flag:
            continue
        ans += 1
    print(ans)
    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
