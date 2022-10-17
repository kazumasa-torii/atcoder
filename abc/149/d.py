"""
貪欲法でとけたのでこういう問題は一度貪欲方で試してみてそれでだめなら
別の考え方を考えるほうが良いかも
"""
def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = list(input())
    score = {"r":  p, "s": r, "p": s}
    tot = 0

    for i in range(k):
        tot += score[t[i]]
    
    for i in range(k, n):
        if t[i-k] == t[i]:
            t[i] = ""
            continue
        tot += score[t[i]]
    print(tot)
    return

if __name__ == '__main__':
    main()