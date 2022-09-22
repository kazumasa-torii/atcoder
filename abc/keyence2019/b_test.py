import sys
import time
from io import StringIO

_INPUT = """\
kaaaeyenceeeee

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    S = input()
    N = len(S)
    
    T = "keyence"
    
    for l in range(N):
        for r in range(l, N):
            if S[:l] + S[r:] == T:
                exit(print("YES"))
    print("NO")
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
