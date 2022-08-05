import sys
import time
from io import StringIO

_INPUT = """\
1079

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
