# 関数

ord_A = ord("A")
print(ord_A)

str = "symbol testnet"

for count in range(len(str)):
    print(str[count])


def spamcaftory():
    print("Spam")


spamcaftory()


def newfoodfactory(times, foodanem="Spam"):
    return foodanem * times


foods = newfoodfactory(4)
print(foods)


def comp_lower(a, b):
    return a - b


a = ["abc", "def", "BCD", "EFG"]
a.sort()
print(a)

# a.sort(comp_lower)
# print(a)

s = set([1, 2, 3, 4])

print(s)

