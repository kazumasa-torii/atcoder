"""
Bit全探索する
行と列を個別に見ていって最終的に同じ内容になっていればOK

Bit全探索はいまいち対応出来ていないので例題対応予定
"""
import sys
input = sys.stdin.readline
def main():
    h1, w1 = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h1)]
    h2, w2 = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(h2)]

    for hs in range(1<<h1):
        for ws in range(1<<w1):
            Is, Js = [], []
            for i in range(h1):
                if (hs>>i) & 1:Is.append(i)
            for j in range(w1):
                if (ws>>j) & 1:Js.append(j)

            if len(Is) != h2: continue
            if len(Js) != w2: continue

            c = [[0] * w2 for i in range(h2)]
            for i in range(h2):
                for j in range(w2):
                    c[i][j] = a[Is[i]][Js[j]]
            if b == c:
                print('Yes')
                exit()
    print('No')
    return

if __name__ == '__main__':
    main()
