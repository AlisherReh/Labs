def compose(f, g):
    def h(x):
        return f(g(x))
    return h

def f(x):
    return x * 2

def g(x):
    return x + 1

h = compose(f, g)

result = h(3)
print(result)  # Output: 8
