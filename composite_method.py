def add_three(x):
    return x + 3


def square(x):
    return x * x


composed_function = lambda x: square(add_three(x))
print(composed_function(3))  # (3 + 3 ) ^2 =36
