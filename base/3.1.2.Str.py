s = 'abababa'
t = 'aba'

# s = input()
# t = input()

count = 0
sub_len = len(t)
for i in range(len(s)):
    if s[i:i+sub_len] == t:
        count += 1
print(count)