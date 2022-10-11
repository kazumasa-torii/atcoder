import sys
import time
from io import StringIO
from typing import List


_INPUT = """\
4 6
1 1 1 1 1 2
1 2 2 2 2 2
1 2 2 3 2 3
1 2 3 2 2 3

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    H, W = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(H)]

    ans = 0
    for bit in range(1, 1 << H):
        hs = []
        for i in range(H):
            if (bit & (1 << i)):
                hs.append(i)
        print(hs)
        cnt = {}
        for j in range(W):
            val = P[hs[0]][j]
            if not all(P[h][j] == val for h in hs):
                continue
            if val not in cnt:
                cnt[val] = 1
            else:
                cnt[val] += 1

        freq_max = 0
        for key in cnt:
            freq_max = max(freq_max, cnt[key])
        ans = max(ans, len(hs) * freq_max)

    print(ans)
    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
