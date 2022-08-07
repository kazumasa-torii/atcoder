import sys
input = sys.stdin.readline
def main():
    a, b, m = map(int, input().split())
    rei = list(map(int, input().split()))
    ren = list(map(int, input().split()))
    wari = []
    for _ in range(m):
        tmp = list(map(int, input().split()))
        wari.append(tmp)
    ans = min(rei) + min(ren)
    
    for i in range(m):
        x, y , c = wari[i]
        ans = min(ans, rei[x-1] + ren[y-1] - c)
    
    print(ans)
    return

if __name__ == '__main__':
    main()
