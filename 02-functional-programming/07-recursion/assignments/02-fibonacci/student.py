def fibonacci_efficient(number):
    a = 0
    b = 1
    if number<=0:
        return 0
    if number == 1:
        return 1
    number -= 1
    while number>=0:
        if number>0:
            a = a + b
            number -= 1
        else:
            return b
        if number>0:
            b = b + a
            number -= 1
        else:
            return a

def fibonacci(number):
    if number <= 0:
        return 0
    if number == 1:
        return 1
    return fibonacci(number-1) + fibonacci(number-2)

def print_fibonacci_test():
    print(fibonacci(0))
    print(fibonacci(1))
    print(fibonacci(2))
    print(fibonacci(3))
    print(fibonacci(4))
    print(fibonacci(5))

def print_fibonacci_efficient_test():
    print(fibonacci_efficient(0))
    print(fibonacci_efficient(1))
    print(fibonacci_efficient(2))
    print(fibonacci_efficient(3))
    print(fibonacci_efficient(4))
    print(fibonacci_efficient(5))

def print_fibonacci():
    print(fibonacci(50))

def print_fibonacci_efficient():
    print(fibonacci_efficient(20577))

# print_fibonacci()
# print_fibonacci_efficient()