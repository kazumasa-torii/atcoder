import sys
import time
from io import StringIO

_INPUT = """\
3141592653589793

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    N = input()
    print(max(int(N[0])-1+9*(len(N)-1),sum(map(int,N))))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
