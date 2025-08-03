def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

print(sum_of_digits(12345))  # Output: 15
