"""
どこをどうDPしているのかわからないので再度履修する
"""

import sys
input = sys.stdin.readline
def main():
    N,M=map(int,input().split())
    a,b,c,d,e,f=map(int,input().split())
    dxy=[(a,b),(c,d),(e,f)]
    S=set()
    for _ in range(M):
        x,y=map(int,input().split())
        S.add((x,y))

    dp=[[1]]
    for i in range(N):
        new_dp=[[0]*(i+2) for _ in range(i+2)]
        for a in range(i+1):
            for b in range(i+1):
                x=a*dxy[0][0]+b*dxy[1][0]+(i-a-b)*dxy[2][0]
                y=a*dxy[0][1]+b*dxy[1][1]+(i-a-b)*dxy[2][1]
                for k in range(3):
                    dx,dy=dxy[k]
                    if not ((x+dx,y+dy) in S):
                        new_dp[a+(1 if k==0 else 0)][b+(1 if k==1 else 0)]+=dp[a][b]
                        new_dp[a+(1 if k==0 else 0)][b+(1 if k==1 else 0)]%=998244353
        dp=new_dp
    print(sum(sum(x) for x in dp)%998244353)
    return

if __name__ == '__main__':
    main()
