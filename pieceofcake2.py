length, vertical_cut, horizontal_cut = input().split()

length = int(length)
vertical_cut = int(vertical_cut)
horizontal_cut = int(horizontal_cut)
half_length = length / 2

longest_vertical = 0
longest_horizontal = 0

if vertical_cut >= half_length:
    longest_vertical = vertical_cut
else:
    longest_vertical = length - vertical_cut
    
if horizontal_cut < half_length:
    longest_horizontal = length - horizontal cut
else:
    longest_horizontal = horizontal_cut
    
print(longest_horizontal * longest_vertical * 4
        
