import sys
import time
from io import StringIO
from turtle import Turtle
from typing import List, Tuple


_INPUT = """\
5 2 3 2

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    a,b,c,d = map(int,input().split())
    for i in range(10**7):
        if a+b*i <= c*i*d:
            print(i)
            sys.exit()
    print(-1)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
