# リスト内包表記

# char_list = []
# for s in "Python":
#     char_list.append(ord(s))
#
# print(char_list)

char_list = [ord(s) for s in "Python"]
print(char_list)


# 2乗した数のリストを作る
exp_2 = [x ** 2 for x in range(10)]
print(exp_2)

# 3乗
exp_3 = [x**3 for x in range(10)]
print(exp_3)

# タプルのリストを作成する.
tap = [(x, x ** 2) for x in range(5)]
print(tap)

# 文字列の反転.
str = u"アイウエオ"
reversed_str = "".join([str[-x-1] for x in range(len(str))])
print(reversed_str)

for x in range(len(str)):
    print("x :", x)
    print("str[x] :", x, str[x])
    print("str[-x] :", -x, str[-x])
    print("str[-x-1] :", -x-1, str[-x-1])

# 回文の判定
palindrome = u"たけやぶやけた"
print(palindrome == "".join([palindrome[-x-1] for x in range(len(palindrome))]))

# 約数を取得する.
value = 12
print([x for x in range(1, value) if value % x == 0])

# こんなイメージ？
# for x in range(1, value):
#   if value % x == 0:
#       return x
# print(x)

l = [x+y for x in (1, 2, 3) for y in (100, 200, 300)]
print(l)


test_list = []
for x in (1, 2, 3):
    for y in (100, 200, 300):
        test_list.append(x+y)

print(test_list)


# 多次元配列の要素を調べる.
# print([(x, y) for x in range(8) for y in range(8) if board[y][x] ==1])

# 約数を調べる（その２）
divisor = [(x, [y for y in range(1, x) if x % y == 0]) for x in range(1, 11)]
print(divisor)

