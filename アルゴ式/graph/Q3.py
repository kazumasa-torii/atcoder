import sys
import time
from io import StringIO
from typing import List
# input = sys.stdin.readline
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

_INPUT = """\
3 3
0 0 2 1
WWW
WBW
WWW

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
