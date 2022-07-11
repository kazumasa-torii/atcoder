import sys
input = sys.stdin.readline
def main():
    N = int(input())
    money = 1
    ans = 0
    while True:
        ans += money
        money += 1
        if ans >= N:
            break
    print(money-1)
    return

if __name__ == '__main__':
    main()
