
fizz_buzz = range(1, 51)

for num in fizz_buzz:
    if num % 15 == 0:
        print("Fizz Buzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)