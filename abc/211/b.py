import sys
input = sys.stdin.readline
def main():
    flag = [False] * 4
    for _ in range(4):
        h = input().strip()
        if h == "H":
            flag[0] = True
        if h == "2B":
            flag[1] = True
        if h == "3B":
            flag[2] = True
        if h == "HR":
            flag[3] = True
    ans = True
    for i in flag:
        if not i:
            ans = False
    print('Yes' if ans else 'No')
    return

if __name__ == '__main__':
    main()
