abc = "abcdefghijklmn"

# 変数を出力
print(abc)

# index 一致する文字列の位置を返却する.
print(abc.index("h"))

# 文字列を全て大文字に変換する.
# lower <-> upper
print(abc.upper())

# 文字列を置換する.
# 一致する文字列を置換する
print(abc.replace('abc', '123'))

linestr = "@" * 20
print(linestr)

print(len(linestr))

print(linestr.index("@"))


