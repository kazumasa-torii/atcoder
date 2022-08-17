import sys
input = sys.stdin.readline
def main():
    a = int(input())
    b = int(input())
    c = int(input())
    x = int(input())

    ans = 0
    for i in range(a+1):
        ac = i * 500
        for j in range(b+1):
            bc = j * 100
            for k in range(c+1):
                cc = k * 50
                if ac + bc + cc == x: ans += 1
    print(ans)
    return

if __name__ == '__main__':
    main()
