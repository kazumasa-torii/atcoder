import sys
import time
from io import StringIO

_INPUT = """\
BBW

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    s = input()
    w = 0
    b = 0
    for i in list(s):
        if i == 'B': b+=1
        else: w+=1
    print(min(w, b) * 2)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
