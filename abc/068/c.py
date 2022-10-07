"""
dfsでも解けるけど2つの定期船ということをうまく使うことができる
島1から行ける定期船の泊まる先からでる定期船を調べて行きたいところがあればそのまま行ける
"""
def main():
    n,m=map(int,input().split())
    s=[[] for i in range(n)]
    for i in range(m) :
        a,b=map(int,input().split())
        s[a-1].append(b-1)

    for i in s[0] :
        if n-1 in s[i] :
            print("POSSIBLE")
            exit()
    
    print("IMPOSSIBLE")
    return

if __name__ == '__main__':
    main()