# 辞書を定義する.
d = {"name": "nomori", "nickname": "nomorin"}
print(d)

# キーを指定して要素を出力する.
print(d['name'])

# 値の更新を行う.
d['name'] = 'Gava dir Gavan'
print(d)

# key-valueの追加.
d['birthyear'] = 1964
print(d)

# 存在しないキーを指定する.エラーになる.
# print(d['birthplace'])

# 辞書の要素を削除する.
del d['nickname']
print(d)

# RSSの擬似データを作成する.
rssitem = {"title": u"Pythonを勉強しておる",
           "link": "https://hogehoge",
           "dc:date": "2020-10-20"}

print(rssitem.keys())

# キーが存在するか確認する.(python3)
print("dc:date" in rssitem.keys())

# 値が存在するか確認する.
print("2020-10-20" in rssitem.values())
# 存在しない場合
print("2020-20" in rssitem.values())

# タプルを定義する.
t = (1, 2, 3, 4, 5)
print(t)

# タプルにおける要素の取り出し.
print(t[1])

print(t[2:4])
