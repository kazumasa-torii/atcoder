"""
エラトステネスの篩
...素数生成プログラム


1.数値を3から見ていき2の倍数と見ている数値の倍数を削除する
1.Nの平方根を求めてそれの2乗は自分になるので平方根以上はみない
1.最後にsetして0を削除する
1.[0, 1, 2...]みたいになっているので2から上のリストを取得させる

"""
from typing import List

n: int = int(input())
p: List[int] = [i for i in range(n+1)]
for i in p[3:]:
    if p[i] % 2 == 0:
        p[i] = 0

root_n: float = n ** 0.5
for i in range(3, n):
    if i > root_n:
        break
    if p[i] != 0:
        for j in range(i, n+1, 2):
            if i * j >= n+1:
                break
            p[i*j] = 0
plist: List[int] = sorted(list(set(p)))[2:]
print(plist)
