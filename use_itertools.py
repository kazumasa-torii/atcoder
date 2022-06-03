import itertools
comb = itertools.combinations('abc', 2)

# ※重複なしの組み合わせ
# printするときには、listにしないと出力されない※イテレーター型なので
print(list(comb))
# [('a', 'b'), ('a', 'c'), ('b', 'c')]

# 重複ありの組み合わせ
comb = itertools.combinations_with_replacement('abc', 2)
print(list(comb))
# [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')]

# 順列の作成
per = itertools.permutations('abc', 2)
print(list(per))

# 直積
A = ['a', 'b', 'c']
B = ['0', '1']

p = itertools.product(A, B)
# [('a', '0'), ('a', '1'), ('b', '0'), ('b', '1'), ('c', '0'), ('c', '1')]
