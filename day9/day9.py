from itertools import pairwise

with open('input.txt', 'r') as file:
    lines = file.readlines()

# Part 1
def get_next(history):
    if all((h == 0 for h in history)):
        return 0
    else:
        return history[-1] + get_next([x2-x1 for x1,x2 in pairwise(history)])

total = 0
for line in lines:
    total += get_next([int(x) for x in line.strip().split()])

print('Part1', total)

# Part 2
def get_next(history):
    if all((h == 0 for h in history)):
        return 0
    else:
        return history[0] - get_next([x2-x1 for x1,x2 in pairwise(history)])
    
total = 0
for line in lines:
    total += get_next([int(x) for x in line.strip().split()])

print('Part2', total)

# Part 1 Iteration
total = 0
for line in lines:
    stack = [[int(x) for x in line.strip().split()]]
    while not all((x == 0 for x in stack[-1])):
        stack.append([x2-x1 for x1,x2 in pairwise(stack[-1])])
    diff = 0
    while len(stack) != 0:
        diff += stack.pop()[-1]
    total += diff
print('Part1 Iteration', total)