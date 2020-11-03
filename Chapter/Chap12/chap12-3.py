# モジュールとクラスの対応
# モジュール             クラス
# モジュールの関数        メソッド
# モジュールの変数        クラスのアトリビュート
# 関数内の変数            インスタンスのアトリビュート
# メソッドもアトリビュートとして扱われる.


class klass():
    # 初期化メソッド.
    def __init__(self):
        # アトリビュートを定義.
        self.spam = 1


ins = klass()
# アトリビュートのリストを表示.
print(dir(ins))

# アトリビュートを追加
ins.egg = 1
# アトリビュートのリストを表示.
print(dir(ins))


class AditionalKlass():
    def foo(self):
        print("this is foo method")


# インスタンスを生成する.
i1 = AditionalKlass()
i2 = AditionalKlass()

# メソッドをコピーする.
i1.bar = i1.foo
i1.bar()

# こっちのインスタンスにはbarメソッドは存在しないためエラーとなる.
# i2.bar()

# アトリビュートは辞書で管理しているため、同名の変数と関数が同一スコープ内に存在すると衝突する.

