import random

numbers = []
for x in range(10000000):
    numbers.append(random.randint(0, 9))

for y in range(10):
    print(f"{y}: {numbers.count(y)}")
