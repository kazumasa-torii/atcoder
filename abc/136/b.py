"""
for 一つで考える
"""
import sys
from typing import List
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
input = sys.stdin.readline

def main():
    n = int(input())
    cnt = 0
    for i in range(1, n+1):
        if len(str(i)) % 2 != 0:
            cnt += 1
    print(cnt)
    return

main()
