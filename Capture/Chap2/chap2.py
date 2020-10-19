# リストの扱い方について
a = [1, 2, 3, 4, 5]
print(a)

# リストの要素を取り出す
print(a[2])

# 最後の要素を取り出す
print(a[-1])

# index Error
# print(a[100])

# スライス
# 文字の間にindexが存在する
# スライスするときは文字の間を指定する.
print(a[1:3])

print(a[3:4])

print(a[3:])

# 配列を結合する.
b = a + [100, 101, 102]

print(b)

# リストの要素を入れ替える.
# これはエラーになる
#c = a + 100
c = a + [100]
print(c)

d = a * 3
print(d)

a[1] = 'Two'
print(a)

# リストの要素を削除する.
del a[2]
print(a)

oilsupply = [271220, 249429, 259705, 262472]
# 配列の最小値を取得する.
print(min(oilsupply))

# 配列の最大値を取得する.
print(max(oilsupply))

# 配列をソートする.(昇順)
oilsupply.sort()
print(oilsupply)

# 配列を逆順にソートする.
oilsupply.reverse()
print(oilsupply)

a.append(100)
print(a)

# 配列が1要素として追加される.
a.append([200, 300, 400])
print(a)



