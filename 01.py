#find smallest number
numbers=[10,23,1,6,9,32,6,77,13]
smallest=numbers[0]
for num in numbers:
    if num<smallest:
        smallest=num
        print("The smallest number is",smallest)