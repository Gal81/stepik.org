def modify_list(l):
    size = len(l)
    i = 0
    while i < size:
        if l[i] % 2:
            l.pop(i)
            size -= 1
        else:
            l[i] = l[i] // 2
            i += 1

lst = [1, 2, 3, 4, 5, 6]
# lst = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
print(modify_list(lst))
print(lst)
modify_list(lst)
print(lst)

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)