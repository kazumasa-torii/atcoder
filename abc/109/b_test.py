import sys
import time
from io import StringIO

_INPUT = """\
8
a
aa
aaa
aaaa
aaaaa
aaaaaa
aaa
aaaaaaa

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    words = []
    words.append(input())
    for _ in range(n-1):
        word = input()
        if word in words:exit(print('No'))
        if word[0] != words[-1][-1]:exit(print('No'))
        words.append(word)
    print('Yes')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
