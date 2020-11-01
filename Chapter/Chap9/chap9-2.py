# スロット.
# アトリビュートの制限をかけることができる.
# スロットで定義された名称以外のアトリビュートは定義できなくなる.


class Klass(object):
    __slots__ = ['a', 'b']

    def __init__(self):
        self.a = 1


i = Klass()
print(i.a)

i.b = 2
print(i.b)

# これはエラーになる.
# i.c = 3

# プロパティ.
# セッターゲッターのこと.


class Prop(object):
    # 初期化処理.
    def __init__(self):
        self.__x = 0

    def getx(self):
        return self.__x

    def setx(self, x):
        self.__x = x

    # ここで紐付けを行う.
    # 中括弧は不要で関数名だけ渡す.
    x = property(getx, setx)


j = Prop()
print(i.x)

j.x = 10
print(j.x)

# print(j._p__x)

