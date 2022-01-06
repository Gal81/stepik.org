# y больше или равно x
# y делится нацело на 5

def closest_mod_5(x):
    y = x
    while True:
        if y % 5 == 0:
            return y
        else:
            y += 1

print(closest_mod_5(16))