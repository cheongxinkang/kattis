number_input = int(input())

for iteration in range(number_input):
    number = int(input())
    if number % 2 != 0:
        print(f"{number} is odd")
    else:
        print(f"{number} is even")
