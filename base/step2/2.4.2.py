dna = input()
# dna = 'aaaabbcaa'
# dna = 'abc'

shift = 0
result = ''
while shift < len(dna):
    lead = dna[shift]
    slice = dna[shift:]

    part = 0
    for next in slice:
        if next == lead:
            part += 1
            shift += 1
        else:
            break
    result += lead + str(part)

print(result)