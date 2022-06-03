import sys
input = sys.stdin.readline
import collections

N = int(input())
nums = list(map(int, input().split()))
c = collections.Counter(nums)

ans = 0
num_max = max(nums)

for j in range(1, num_max+1):
    for k in range(1, num_max//j+1):
        i = k*j
        if c[i] and c[j] and c[k]:
            ans += c[i] *c[j] * c[k]
print(ans)















# n = int(input())
# a = list(map(int,input().split()))
# c = collections.Counter(a) # dict作成する（現在ある数字の内容を数を取得させる）

# ans = 0
# ma = max(a) # 最大値を取得してその数字まで回せるようにする
# for j in range(1,ma+1): # 全探索させる数字
#     for k in range(1,ma//j +1): # １からkまでを全探索(i/j=kなのでkは整数でありiにとっての約数になる)
#         i = j * k # i/j=k 変換 => i=k*j
#         if c[i] != 0 and c[j] != 0 and c[k] != 0: # 各整数の値がdictに存在するか確認する
#             ans += c[i]*c[j]*c[k] # 存在した数字の量に比例して組み合わせの数を算出してプラスする
# print(ans)
