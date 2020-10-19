#!/usr/bin/env python
# 条件分岐.

# year = 1900
# if year == 1868:
#     print(u"明治元年")
# else:
#     if year ==1912:
#         print(u"大正元年")
#     else:
#         print(u"明治", year - 1867, u"年")

# elif を利用したバージョン.
year = 1912
if year == 1868:
    print(u"明治元年")
elif 1869 <= year <= 1911:
    print(u"明治", year - 1867, u"年")
else:
    print(u"大正元年")


# findメソッドを使用する.
s = "this is ASCII string"
if s.find("ASCII") != -1:
    print("I found ASCII")

# in メソッドを利用する.
if "ASCII" in s:
    print("I found ASCII")

# 型の違う変数を比較する.
num_one = 1
str_one = "1"
print(num_one == str_one)

# 変換して比較(int to str)
print(str(num_one) == str_one)
# 変換して比較(str to num)
print(num_one == int(str_one))


