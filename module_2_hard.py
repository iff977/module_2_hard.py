def find_pairs(n):
    pairs = []
    for i in range(1, n // 2 + 1):
        j = n - i
        if n % (i + j) == 0:
            pairs.append(i)
            pairs.append(j)
    return pairs
import random

num = random.randint(3, 20)
print("Число из первой вставки: ", num)
result = find_pairs(num)
if result:
    for pair in result:
        print(pair)
else:
    print("нет пар!")
