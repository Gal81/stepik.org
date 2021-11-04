def f(x):
    if x <= -2:
        return 1 - (x + 2) ** 2
    if x > -2 and x <= 2:
        return -(x / 2)
    if x > 2:
        return (x - 2) ** 2 + 1