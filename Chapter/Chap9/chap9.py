class Prism:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def content(self):
        return self.depth * self.height * self.depth


class Cube(Prism):
    def __init__(self, length):
        # スーパークラスのコンストラクタを指定する方法.
        Prism.__init__(self, length, length, length)

        # スーパークラスのアトリビュートにアクセスする方法.
        # self.width = self.height = self.depth = length


# インスタンスを作成してメソッドを呼び出す.
c = Cube(20)
print(c.content())


