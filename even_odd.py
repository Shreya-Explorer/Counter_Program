import sys
if len(sys.argv)==2:
    script_name=sys.argv[0]
    num=int(sys.argv[1])
else:
    script_name=sys.argv[0]
    num=23
even=0
odd=0
if num % 2 == 0:
    even=num
else:
    odd =num
print("Numbers:", num)
print("Count of Even Numbers:", even)
print("Count of Odd Numbers:", odd)
