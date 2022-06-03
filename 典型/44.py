import sys
input = sys.stdin.readline

limit, Q = map(int, input().split())
nums = list(map(int, input().split()))

index = 0
for _ in range(Q):
    q, x, y = map(int, input().split())
    x = (x - index - 1) % limit
    y = (y - index - 1) % limit
    if q == 2:
        index += 1
    elif q == 1:
        tmp_x = nums[x]
        tmp_y = nums[y]
        nums[x] = tmp_y
        nums[y] = tmp_x
    elif q == 3:
        print(nums[x])
