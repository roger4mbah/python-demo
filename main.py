
sentinel = 100


for i in range(1, sentinel + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzFuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Fuzz")
    else:
        print(i)
