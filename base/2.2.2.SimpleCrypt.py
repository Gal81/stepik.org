from simplecrypt import decrypt

encrypted = ''
with open('base\\dump\\encrypted.bin', 'rb') as file:
    encrypted = file.read()

passwords = ''
with open('base\\dump\\passwords.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    passwords = data.strip().split('\n')

for password in passwords:
    try:
        plaintext = decrypt(password, encrypted).decode('utf8')
    except Exception:
        pass
    else:
        print(plaintext)