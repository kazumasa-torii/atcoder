import sys
import time
from io import StringIO
from typing import List
# input = sys.stdin.readline
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

_INPUT = """\
0601889

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    S = list(input().strip())
    han = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
    ans = []
    l = len(S)
    for i in range(l-1, -1, -1):
        ans.append(han[S[i]])
    print(''.join(ans))
    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
