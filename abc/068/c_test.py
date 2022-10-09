"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
5 5
1 3
4 5
2 3
2 4
1 4

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n,m=map(int,input().split())
    s=[[] for i in range(n)]
    for i in range(m) :
        a,b=map(int,input().split())
        s[a-1].append(b-1)

    for i in s[0] :
        if n-1 in s[i] :
            print("POSSIBLE")
            exit()
    
    print("IMPOSSIBLE")
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
