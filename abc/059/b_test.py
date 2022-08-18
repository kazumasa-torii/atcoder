import sys
import time
from io import StringIO

_INPUT = """\
9720246
22516266

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    a = int(input())
    b = int(input())
    if a > b: print('GREATER')
    elif a < b: print('LESS')
    else: print('EQUAL')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
