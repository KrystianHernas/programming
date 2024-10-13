from re import X


def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

# Using the generator
counter = count_up_to(5)
for number in counter:
    print(number)

squares = (x**2 for x in range(10))

# Using the generator
for y in squares:
    print(y)
