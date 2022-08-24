"""
sortして愚直に全探索できるか考える
その後に難しそうであれば下記アルゴリズムを考える

共通
全探索,二部探索,累積和,いもす法,順列全探索,区間スケジューリング,貪欲法,鳩の巣原理

グラフ関係
DFS,BFS,ダイクストラ法,ワーシャルフロイド法,トポロジカルソート

DP
区間,bit,ナップサック,桁

数学
約数,素数判定法,mod,組み合わせ,幾何

その他
クラスカル法,木,Union-find
"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
2 2
1 1 1 2 1 3
1 2
2 2

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

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
    print(f'[Sec] {str(time.time() - StartTime)}')
