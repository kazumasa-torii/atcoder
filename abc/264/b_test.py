import sys
import time
from io import StringIO

_INPUT = """\
4 5

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    r, c = map(lambda x:int(x)-1, input().split())
    maps = [
    ['b','b','b','b','b','b','b','b','b','b','b','b','b','b','b',],
    ['b','w','w','w','w','w','w','w','w','w','w','w','w','w','b',],
    ['b','w','b','b','b','b','b','b','b','b','b','b','b','w','b',],
    ['b','w','b','w','w','w','w','w','w','w','w','w','b','w','b',],
    ['b','w','b','w','b','b','b','b','b','b','b','w','b','w','b',],
    ['b','w','b','w','b','w','w','w','w','w','b','w','b','w','b',],
    ['b','w','b','w','b','w','b','b','b','w','b','w','b','w','b',],
    ['b','w','b','w','b','w','b','w','b','w','b','w','b','w','b',],
    ['b','w','b','w','b','w','b','b','b','w','b','w','b','w','b',],
    ['b','w','b','w','b','w','w','w','w','w','b','w','b','w','b',],
    ['b','w','b','w','b','b','b','b','b','b','b','w','b','w','b',],
    ['b','w','b','w','w','w','w','w','w','w','w','w','b','w','b',],
    ['b','w','b','b','b','b','b','b','b','b','b','b','b','w','b',],
    ['b','w','w','w','w','w','w','w','w','w','w','w','w','w','b',],
    ['b','b','b','b','b','b','b','b','b','b','b','b','b','b','b',],
    ]
    print('white' if maps[r][c] == 'w' else 'black')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
