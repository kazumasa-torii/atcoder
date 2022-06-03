"""
辞書型で存在しないキーでも参照してもエラーが無い
"""
from collections import defaultdict

A=[int(i) for i in input().split()]
dd=defaultdict(int)
for a in A:
    dd[a]+=1

"""
個数カウントを行うときに使用することが多い
特に使用しなくても良いかも
"""
from collections import Counter
l=['a','b','b','c','b','a','c','c','b','c','b','a']
S=Counter(l)#カウンタークラスが作られる。S=Counter({'b': 5, 'c': 4, 'a': 3})
print(S.most_common(2)) #[('b', 5), ('c', 4)]
print(S.keys()) #dict_keys(['a', 'b', 'c'])
print(S.values()) #dict_values([3, 5, 4])
print(S.items()) #dict_items([('a', 3), ('b', 5), ('c', 4)])
