# 標準ライブラリについて.
# StringIOはpython3 で廃止されたらしい.
# from StringIO import StringIO
from io import StringIO

# メソッドを渡す.
f = StringIO()
# 文字列を書き込む.
f.write("1234567890")
# シーク位置を先頭に移動する.
f.seek(0)
# ストリームを読み込む.
res = f.read()
print(res)

# シーク位置を変更してみる
# read ではシーク位置以降の文字列が読み込まれる.
f.seek(2)
# 引数を与えることで、何文字目まで読み込むのか指定できる
res = f.read(2)
print(res)

# シークの位置に関係なく全ての文字列を取得する.
res = f.getvalue()
print(res)

# メモリを解放する.
f.close()

# クローズ後に参照はできない.
# res = f.read()




