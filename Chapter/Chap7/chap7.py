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

