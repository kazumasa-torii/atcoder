import sys
input = sys.stdin.readline
def main():
    n = int(input())
    li = [1, 2, 4, 8, 16, 32, 64]
    li.sort(reverse=True)
    for i in li:
        if i <= n:
            print(i)
            break
    return

if __name__ == '__main__':
    main()
