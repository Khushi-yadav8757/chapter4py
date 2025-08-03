def find_missing(lst, n):
    total = n * (n + 1) // 2
    return total - sum(lst)

print(find_missing([1, 2, 3, 5], 5))  # Output: 4
