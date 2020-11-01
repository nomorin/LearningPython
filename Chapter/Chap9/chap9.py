class Prism:
    def __init__(self, width, height, depth, unit='cm'):
        self.width = width
        self.height = height
        self.depth = depth
        self.unit = unit

    def content(self):
        return self.depth * self.height * self.depth

    def unit_content(self):
        return str(self.content()) + self.unit


class Cube(Prism):
    def __init__(self, length):
        # スーパークラスのコンストラクタを指定する方法.
        # Prism.__init__(self, length, length, length)

        # スーパークラスのアトリビュートにアクセスする方法.
        # self.width = self.height = self.depth = length

        # superを利用してスーパークラスにアクセスする方法.
        # selfはインスタンス 自身(javaのthis)
        # superは継承している親クラスを参照する.
        super(Cube, self).__init__(length, length, length)


# インスタンスを作成してメソッドを呼び出す.
c = Cube(20)
print(c.unit_content())


