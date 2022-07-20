import sys
input = sys.stdin.readline
def main():
    n, x = map(int, input().split())
    li = list(map(int, input().split()))
    li.insert(0, 0)
    for i in range(len(li)):
        if i == 0 or i % 2 != 0:
            continue
        li[i] -= 1
    print('Yes' if sum(li) - x <= 0  else 'No')
    return

if __name__ == '__main__':
    main()
