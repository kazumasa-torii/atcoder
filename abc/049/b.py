import sys
input = sys.stdin.readline
def main():
    h, w = map(int, input().split())
    maps = []
    for _ in range(h):
        a = input()
        maps.append(a)
        maps.append(a)

    for i in maps:
        print(i)
    return

if __name__ == '__main__':
    main()
