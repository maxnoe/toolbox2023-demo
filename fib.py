def fibonacci(i):
    n = 0
    if i == 0:
        return n

    previous = 0
    n = 1
    if i == 1:
        return n

    for _ in range(2, i):
        n, previous = n + previous, n
    
    return n


if __name__ == "__main__":
    for i in range(35):
        print(fibonacci(i))