"""

"""
import sys
import time
from io import StringIO
from typing import List


_INPUT = """\
abbaac
abbbbaaac

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    def rle(s):
        li = []
        li.append([s[0][0], 1])
        for c in range(1, len(s)):
            print(c)
            if len(s) > 0 and li[-1][0] == s[c]:
                li[-1][1] += 1
            else:
                li.append([s[c], 1])
        return li

    def solve(a, b):
        al = len(a)
        bl = len(b)
        if al != bl: return False
        for i in range(al):
            if a[i][0] != b[i][0]: return False
            int_a = a[i][1]
            int_b = b[i][1]
            if int_a == 1:
                if int_b != 1: return False
                else:
                    if int_b < int_a: return False
        return True

    S = input().strip()
    T = input().strip()
    s_list = rle(S)
    t_list = rle(T)
    print('Yes' if solve(s_list, t_list) else 'No')

    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
