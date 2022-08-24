import sys
import time
from io import StringIO

_INPUT = """\
8
buffalo
buffalo
buffalo
buffalo
buffalo
buffalo
buffalo
buffalo

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
