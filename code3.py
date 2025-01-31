def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
for number in range(1, 100):
    if is_prime(number):
        print(number)