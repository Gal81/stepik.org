num = 1
def primes():
    global num

    while True:
        num += 1
        is_prime = True

        for i in range(2, num):
            if (num % i) == 0:
                is_prime = False
                break

        if is_prime:
            yield num

# print(next(primes()))
# print(next(primes()))
# print(next(primes()))