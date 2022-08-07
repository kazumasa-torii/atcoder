import sys
input = sys.stdin.readline
import itertools
def main():
    n = int(input())
    nums = [i for i in range(1, n+1)]
    ptr = list(itertools.permutations(nums, n))
    ptr.sort()
    ans = 0
    for _ in range(2):
        tmp = list(map(int, input().split()))
        for i in range(len(ptr)):
            flag = True
            for x, y in zip(tmp, ptr[i]):
                if x != y:
                    flag = False
                    break
            if flag: break
        ans = abs(ans - i)
    print(ans)
    return

if __name__ == '__main__':
    main()
