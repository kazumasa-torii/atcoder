"""
約数列挙
"""
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        # 小さい数字順からのバターン
        if n % i == 0:
            lower_divisors.append(i)
            # 大きい数字順からのパターン
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    # 最後に両方くっつけて昇順にて並び替えて終わり
    return lower_divisors + upper_divisors[::-1]

if __name__ == '__main__':
    print(make_divisors(10))
