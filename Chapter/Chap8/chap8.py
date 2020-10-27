from decimal import *

# lang_list = ['Java', 'perl', 'PHP', 'Python', 'Ruby']
#
# print(lang_list)
#
# lang_list.remove('Java')
# print(lang_list)

d = Decimal(10)
print(d)

# 整数の加算.
print(d + 20)

# 小数の加算.
# 小数の場合は文字列をDecimalに渡す
print(d + Decimal("0.2"))

# 平方根の計算
print(d.sqrt())



