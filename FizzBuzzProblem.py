# Write a program that automatically prints the solution to a FizzBuzz game.
# The rules of the FizzBuzz game is as follows:
# 1. Program should print each number from 1 to 100 in turn, and include number 100
# 2. When the number is divisible by 3, then it should print "Fizz" instead of printing the number
# 3. When the number is divisible by 5, then it should print "Buzz" instead of printing the number
# 4. When the number is divisible by both 3 and 5, then it should print "FizzBuzz" instead of printing the number

# code
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
