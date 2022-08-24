import sys
input = sys.stdin.readline
def main():
    n = int(input())
    rui = [1, 4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100, 121, 125, 128, 144, 169, 196, 216, 225, 243, 256, 289, 324, 343, 361, 400, 441, 484, 512, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1000,]
    for i in range(n, -1, -1):
        if i in rui:exit(print(i))
    return

if __name__ == '__main__':
    main()
