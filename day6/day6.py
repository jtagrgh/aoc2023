import math

with open('input.txt', 'r') as file:
    lines = file.readlines()

# Part 1
data = list(zip([int(x) for x in lines[0].split()[1:]], [int(x) for x in lines[1].split()[1:]]))

total = 1
for time, best in data:
    left_root = (-time + math.sqrt(time**2 - 4*best)) / (-2)
    right_root = (-time - math.sqrt(time**2 - 4*best)) / (-2)
    int_left_root = math.floor(left_root + 1)
    int_right_root = math.ceil(right_root - 1)
    solutions =int_right_root - int_left_root + 1
    total *= solutions

print('Part 1', total)


# Part 2
time = int(''.join(lines[0].split()[1:]))
best = int(''.join(lines[1].split()[1:]))

left_root = (-time + math.sqrt(time**2 - 4*best)) / (-2)
right_root = (-time - math.sqrt(time**2 - 4*best)) / (-2)
int_left_root = math.floor(left_root + 1)
int_right_root = math.ceil(right_root - 1)
solution = int_right_root - int_left_root + 1

print('Part 2', solution)