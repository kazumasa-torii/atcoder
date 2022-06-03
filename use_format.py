# 基本
print("aaaは{0}です。 BBBは{1}です".format('AAA', 'bbb'))

# 文字列型
# "s" 文字列
print("aaaは{:s}です。 BBBは{1}です".format('AAA', 'bbb'))

# 整数型
"""
"b" 2進数
"c" 文字。数値を対応する Unicode 文字に変換
"d" 10進数
"o" 8進数
"x" 16進数。a～fは小文字
"X" 16進数。A～Fは大文字
"n" 数値。現在のロケールに従い、区切り文字を挿入することを除けば "d" と同じ
"""
print("aaaは{:b}です。 BBBは{:x}です".format(111, 123))
# 2進数のプリフィックスを外した状態せ記載できる
ni = format(111, 'b')
print("aaaは{ni}です。")

