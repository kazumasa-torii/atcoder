"""
sは後ろの部分から
tは前の部分から
両方を突合させて一番長い長さを取得できたら2nから差し引く
"""

import sys
input = sys.stdin.readline
def main():
    n = int(input())
    s = input()
    t = input()
    
    ans = 2*n
    cnt = 0
    for i in range(n):
        if s[n-i-1:] == t[:i+1]:
            cnt = max(cnt, i+1)
    print(ans-cnt)
    return

if __name__ == '__main__':
    main()