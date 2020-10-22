# 組み込み関数

seq = ["one", "two", "three"]

counter = 0
for item in seq:
    print(counter, item)
    counter += 1


for count in range(len(seq)):
    print(count, seq[count])


for count, item in enumerate(seq):
    print(count, item)


# zip python3から変わったらしい
a = ([1, 2, 3, 4])
b = (['a', 'b', 'c', 'd'])

# print(zip([1, 2, 3, 4], ['a', 'b', 'c', 'd']))
for aa, bb in zip(a, b):
    print(aa, bb)


def multi_return():
    return 1, 2, 3


hoge , fuga, piyo = multi_return()

print(hoge, fuga, piyo)

# こっちはタプル.
def foo(a, b, *values):
    print(a, b, values)


foo(1, 2, 3, 4, 5)
# foo(1, 2, keyword=3)

# こっちは辞書.
def bar(a, b, **kwargs):
    print(a, b, kwargs)

# **の場合だと引数を超えた部分は受け取られない
# bar(1, 2, 3, 4, 5)

# **引数の部分は辞書になる
bar(1, 2, z=1, y=2)
