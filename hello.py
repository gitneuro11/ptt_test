def calculator(x, y):
    def multiply(a, b):
        return a * b
    return multiply(x, y) + (x + y)

print(calculator(3, 4))
