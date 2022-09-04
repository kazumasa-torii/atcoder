import sys
import time
from io import StringIO

_INPUT = """\
Wednesday

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    m = {'Monday':5, 'Tuesday':4, 'Wednesday':3, 'Thursday':2, 'Friday':1}
    print(m[input()])
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
