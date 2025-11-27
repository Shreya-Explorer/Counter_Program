# even_odd_count.py
import sys

# Take all arguments except script name
numbers = [int(x) for x in sys.argv[1:]]

even = 0
odd = 0

for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even count:", even)
print("Odd count:", odd)
