def febonacci(n):
    a = 1
    b = 1
    for c in range(n):
        yield a
        a, b = b, a+b


for x in febonacci(5):
    print(x)
