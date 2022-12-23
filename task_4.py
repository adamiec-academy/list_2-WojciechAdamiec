def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_diabolic(n):
    return "666" in str(n)


def test():
    count = 0
    for i in range(1, 100001):
        if is_diabolic(i) and is_prime(i):
            count += 1
            print(i)
    print(f"Count: {count}")
