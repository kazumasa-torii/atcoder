import sys
input = sys.stdin.readline
def main():
    x = list(input().strip())
    for i in range(4):
        x[i] = int(x[i])
    nums = {0:1, 1:2, 2:3, 3:4, 4:5, 5:6, 6:7, 7:8, 8:9, 9:0}
    sx = set(x)
    if len(sx) == 1:
        print('Weak')
        exit()
    flag = 0
    for i in range(1, 4):
        if x[i] == nums[x[i-1]]: flag += 1
    print('Strong' if flag != 3 else 'Weak')
    return

if __name__ == '__main__':
    main()
