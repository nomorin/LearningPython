
class MyClass:
    # pass :空の関数やクラスを定義するためのもの
    # pass は　null 操作.
    # 何もしたくない時に使用する.
    pass

i = MyClass()

# アトリビュートに値を保存する.
# アトリビュートは個々のインスタンスに別々に作られる.
i.value = 5

print(i.value)


class MyClass2:
    # コンストラクタのようなもので、インスタンスが生成されたタイミングで初期化処理を行う.
    # 引数には、selfを渡してインスタンス事態を操作することができる.
    # self <- インスタンス情報が格納されている.
    # tip : メタクラスというものが存在する.
    def __init__(self):
        # アトリビュートに代入
        self.value = 0
        print("this is __init__ method")


my_class2 = MyClass2()

