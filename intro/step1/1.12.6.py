a = int(input())

text1 = 'программист' # 1
text2 = 'программиста' # 2,3,4
text3 = 'программистов' # 0,5,6,7,8,9 | 10,11,12,13,14,15,16,17,18,19,20

def get_rest(value):
    div = 10
    rest = value

    if rest > 100:
        rest = rest - 100
    if rest > 20:
        rest = rest % div

    return rest

def msg(value):
    rest = get_rest(value)

    if rest in [0,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
        return text3

    elif rest in [2,3,4]:
        return text2

    else:
        return text1

print(a, msg(a))

# for x in range(0, 1000):
#     rest = get_rest(x)

#     print(rest, '>>', x, msg(rest))