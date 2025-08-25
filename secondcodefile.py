numbers = [1, 2, 3, 4, 2, 5, 3, 6, 1]

seen = set()
duplicates = set()

for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print("Duplicate numbers:", duplicates)

Output = Duplicate numbers: {1, 2, 3}

