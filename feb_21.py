# decorators

# function in function

def check1(func):
    def inner(a,b):
        print("in decorator")
        if a > 0 and b > 0:
            print(func(a,b))
    return inner

@check1
def sum1(a,b):
    print("in sum")
    return a*b

sum1(1,2)

# def make_pretty(func):

#     def inner():
#         print("I got decorated")
#         func()
#     return inner

# @make_pretty
# def ordinary():
    # print("I am ordinary")

# ordinary()  



def factorial_decorator(func):
    def inner(n):
        if n < 0:
            return 1
        elif n == 0 or n == 1:
            return 1
        else:
            return func(n)
    return inner

@factorial_decorator
def calculate_factorial(n):
    return n * calculate_factorial(n - 1)

# Test the decorated function

result = calculate_factorial(4)
print(f"Factorial: {result}")
