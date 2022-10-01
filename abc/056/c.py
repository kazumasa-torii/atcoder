import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def main():
    x = int(input())
    total = 0
    i = 1
    while True:
        total += i
        if total >= x:break
        i += 1
    print(i)
    return

if __name__ == '__main__':
    main()