import sys
import time
from io import StringIO

_INPUT = """\
RU WU WD

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

import sys

def main():
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
