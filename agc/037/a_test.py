import sys
import time
from io import StringIO

_INPUT = """\
aabbaa

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    s = input()
    ans = [s[0]]
    tmp = str()

    for i in range(1, len(s)):
        tmp += s[i]
        if tmp != ans[-1]:
            ans.append(tmp)
            tmp = str()
    print(len(ans))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
