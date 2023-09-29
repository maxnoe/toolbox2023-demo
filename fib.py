def fibonacci(n):
    if n < 2:
        return n
    
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    for i in range(10):
        print(fibonacci(i))