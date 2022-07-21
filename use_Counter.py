"""
collections.Counter()にリストやタプルを渡すと、
Counterオブジェクトが生成される。
Counterは辞書型dictのサブクラスで、
キーに要素、値に出現回数という形のデータを持つ。
"""

import collections

l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']

c = collections.Counter(l)
print(c)
# Counter({'a': 4, 'c': 2, 'b': 1})

print(type(c))
# <class 'collections.Counter'>

print(issubclass(type(c), dict))
# True

print(c['a'])
# 4

print(c['b'])
# 1

print(c['c'])
# 2

print(c['d'])
# 0

"""
keys(), values(), items()などの辞書型のメソッドも使える。
"""
print(c.keys())
# dict_keys(['a', 'b', 'c'])

print(c.values())
# dict_values([4, 1, 2])

print(c.items())
# dict_items([('a', 4), ('b', 1), ('c', 2)])

"""
Counterにはmost_common()メソッドがあり、
(要素, 出現回数)
という形のタプルを出現回数順に並べたリストを返す。

出現回数が最も多いものは[0]、
最も少ないものは[-1]のように
インデックスを指定して取得できる。
要素だけ、出現回数だけを取得したい場合はさらにインデックスを指定すればOK。
"""

print(c.most_common())
# [('a', 4), ('c', 2), ('b', 1)]

print(c.most_common()[0])
# ('a', 4)

print(c.most_common()[-1])
# ('b', 1)

print(c.most_common()[0][0])
# a

print(c.most_common()[0][1])
# 4

"""
出現回数の少ない順に並べ替えたい場合は増分を-1としたスライスを使う。
"""
print(c.most_common()[::-1])
# [('b', 1), ('c', 2), ('a', 4)]

"""
リストやタプルに重複しない要素（一意な要素）が何個あるか（何種類あるか）
をカウントする場合、上述のCounterかset()を使う。
"""

l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']
c = collections.Counter(l)

print(len(c))
# 3
