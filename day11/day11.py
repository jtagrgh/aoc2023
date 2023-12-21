from collections import deque

with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

def transposed(matrix):
    return [list(i) for i in zip(*matrix)]

def expanded(matrix):
    matrix = matrix.copy()
    offset = 0
    for i, row in enumerate(matrix.copy()):
        if all(x == '.' for x in row):
            matrix.insert(i + offset, row)
            offset += 1
    return matrix

expanded_lines = transposed(expanded(transposed(expanded(lines))))

galaxies = []
for j in range(len(expanded_lines)):
    for i in range(len(expanded_lines[0])):
        if expanded_lines[j][i] == '#':
            galaxies.append((j,i))

total = 0
for i, g1 in enumerate(galaxies):
    for g2 in galaxies[i+1:]:
        x_diff = abs(g2[1] - g1[1])
        y_diff = abs(g2[0] - g1[0])
        total += x_diff + y_diff

print('Part1', total)

empty_xs = [i for i, row in enumerate(transposed(lines)) if all(x == '.' for x in row)]
empty_ys = [i for i, row in enumerate(lines) if all(x == '.' for x in row)]

galaxies = []
for j in range(len(lines)):
    for i in range(len(lines[0])):
        if lines[j][i] == '#':
            galaxies.append((j,i))

total = 0
for i, g1 in enumerate(galaxies):
    for g2 in galaxies[i+1:]:
        x_interval = (min(g1[1], g2[1]), max(g1[1], g2[1]))
        n_empty_x_in = len([x for x in empty_xs if x > x_interval[0] and x < x_interval[1]])
        y_interval = (min(g1[0], g2[0]), max(g1[0], g2[0]))
        n_empty_y_in = len([y for y in empty_ys if y > y_interval[0] and y < y_interval[1]])
        x_diff = x_interval[1] - x_interval[0] - n_empty_x_in + n_empty_x_in*1000000
        y_diff = y_interval[1] - y_interval[0] - n_empty_y_in + n_empty_y_in*1000000
        total += x_diff + y_diff

print('Part2', total)