from builtins import print


class Prism:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def content(self):
        """
        引数selfは自動的に代入されるためself は呼び出し側では記載しなくて良い.
        :return: 体積.
        """
        return self.width * self.height * self.depth


p = Prism(10, 10, 10)
print(p.content())

# アトリビュートの値を取得する.
print("height:", p.height)
print("width:", p.width)
print("depth:", p.depth)

# アトリビュートは書き換え可能.
p.width = 20
print(p.content())


# カプセル化について
# _ クラスの外部からは書き換えてはいけないアトリビュート（暗黙のルール）
# __ クラスの外部から書き換えられないようにしているアトリビュート


class Triangle:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def calc(self):
        return self.__height * self.__width / 2


a = Triangle(2, 10)
print(a.calc())

# アクセス可能
# a._height

# アクセス不可能（隠蔽化されているものを探すことはできる）
# a.__height


