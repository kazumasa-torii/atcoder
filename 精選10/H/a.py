import sys
input = sys.stdin.readline
def main():
    n = int(input())
    x = set()
    for _ in range(n):
        x.add(int(input()))
    print(len(x))
    return

if __name__ == '__main__':
    main()
