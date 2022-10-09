"""

"""
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    li = list(map(int, input().split()))
    li.sort()
    if N <= 2:
        print(max(li))
        return
    sum_num = 0
    if sum(li) % 2 != 0:
        sum_num = sum(li) // 2 + 1
    else:
        sum_num = sum(li) // 2
    print(sum_num)
    return

main()
