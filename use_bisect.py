"""
bisectには挿入箇所を探索する関数(bisect)
bisect_left
bisect_right
bisect

探索と挿入を同時に行う(insort)
insort_left
insort_right
insort
"""
import bisect 
A = [1, 2, 3, 3, 3, 4, 4, 6, 6, 6, 6]

"""
bisect.bisect_left(a, x, lo=0, h=len(a)) 挿入箇所がxより左のindexの値を出す
bisect.bisect_right(a, x, lo=0, h=len(a)) 挿入箇所がxより右のindexの値を出す

引数は以下になります(他の関数においても同様)
a: ソート済みリスト
x: 挿入したい値
lo: 探索範囲の下限
hi: 探索範囲の上限
(lo, hiはスライスと同様の指定方法)
"""
index = bisect.bisect_left(A, 3)
# print(index) -> 2(要素の中でも一番左(前)の挿入箇所がかえる)

index = bisect.bisect_right(A, 3)
# print(index) -> 5(要素の中でも一番右(後)の挿入箇所がかえる)
