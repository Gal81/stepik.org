abc = input() # 'abcd'
code = input() # '*d%#'

data_encode = input() # 'abacabadaba'
data_decode= input() # '#*%*d*%'

result_encode = ''
result_decode = ''
for ch in data_encode:
    index = abc.index(ch)
    result_encode += code[index]

for ch in data_decode:
    index = code.index(ch)
    result_decode += abc[index]

print(result_encode)
print(result_decode)

# *d*%*d*#*d*
# dacabac