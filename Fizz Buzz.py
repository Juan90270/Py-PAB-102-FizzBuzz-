
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


"""
Program that iterates over the integers 1 through 50 
using a loop.

For numbers which are multiples of both 3 
and 5 print “FizzBuzz” in the output.  For example, 
15 is divisible by both 3 and 5, so instead of 
printing 15, print "FizzBuzz".  For numbers which 
are multiples of 3 but not 5 (such as 42) print 
“Fizz” instead of the number.  For the numbers 
that are multiples of 5 but not 3 (such as 20) 
print “Buzz” instead of the number.

All of the integers which are not multiples of 
3 or 5 should just be printed as themselves.
"""