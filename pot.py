number_input = int(input())

numbers = []

for i in range(number_input):
    numbers.append((input()))

value = 0
 
for number in numbers:
    power = int(number[-1])
    length = len(number)
    integer = int(number[:length-1])
    value = value + (integer ** power)
    
print(value)
