gc = input().lower()
# gc = 'acggtgttat'

counter = 0
for char in gc:
    if char == 'g' or char == 'c':
        counter += 1

print(counter / len(gc) * 100)
