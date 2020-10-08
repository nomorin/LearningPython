# fizzbuzz.
for idx in range(1, 101):
    if idx % 3 == 0 and idx % 5 == 0:
        print("fizz buzz")
    elif idx % 3 == 0:
        print("fizz")
    elif idx % 5 == 0:
        print("buzz")
    else:
        print(idx)

