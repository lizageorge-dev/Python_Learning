def greet(name):
    print("Hello "+name)

#factorial(n): Returns the factorial of n
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    