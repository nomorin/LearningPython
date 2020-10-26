# イテレータ.
ite = iter([1, 2, 3])
print(ite.__next__())
print(ite.__next__())
print(ite.__next__())
# print(ite.__next__())

dictionary = {1:1, 2:2, 3:3}
for key in dictionary:
    print(key)


# ジェネレータ
# Pythonのelse文はforとも組み合わせ可能.

# for ループが終了したタイミングで実行.
# while falseになったタイミングで実行.
# breakで終了した場合は実行されない.
def get_primes(x = 2):
    while True:
        for i in range(2, x):
            # print("for i:", i, "x is ", x)
            if x % i == 0:
                # print("break!!!")
                break
        else:
            # print("return yield")
            yield x

        x += 1


i = get_primes()
for count in range(10):
    print("primes :", i.__next__())
    # print("")

# practice
print("".join([chr(c) for c in range(32, 127)]))


