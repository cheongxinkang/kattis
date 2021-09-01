long_name = input()

short_name = ''

for i in long_name:
    if i.isupper():
        short_name = short_name + i

print(short_name)
