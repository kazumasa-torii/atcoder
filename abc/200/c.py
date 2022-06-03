import sys
input = sys.stdin.readline
size = int(input())
nums = list(map(int, input().split()))
num_dict = {i:0 for i in range(201)}
ans = 0
for i in nums:
    num_dict[i%200] += 1
for i in num_dict:
    if num_dict[i] == 0:
        continue
    ans += int((num_dict[i] * (num_dict[i] - 1)) / 2)
print(ans)
