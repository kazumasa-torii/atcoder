import sys
input = sys.stdin.readline
def main():
    a, b = map(int, input().split())
    x = input().strip()
    flag = True
    for i in range(len(x)):
        if not x[i].isdecimal() and a != i:
            flag = False
            break
        if a == i and x[i].isdecimal():
            flag = False
            break
    print('Yes' if flag else 'No')
    return

if __name__ == '__main__':
    main()
