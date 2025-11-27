import sys
args = sys.argv[1:]
numbers = [int(num) for num in args]
even = 0
odd = 0
for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
print("Numbers:", numbers)
print("Count of Even Numbers:", even)
print("Count of Odd Numbers:", odd)
