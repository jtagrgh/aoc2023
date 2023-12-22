from collections import Counter

patterns = [[]]

with open('input.txt', 'r') as file:
    for line in file.read().splitlines():
        if line == '':
            patterns.append([])
        else:
            patterns[-1].append(line)

def transposed(matrix):
    return [list(x) for x in zip(*matrix)]

def is_mirrored(matrix, i):
    n_above = i
    n_below = len(matrix) - i - 2
    m = min(n_above, n_below)
    for j in range(m+1):
        if matrix[i-j] != matrix[i+1+j]:
            return False
    return True

total = 0
for pattern in patterns:
    for i in range(0, len(pattern)-1):
        if is_mirrored(pattern, i):
            total += 100 * (i+1)
    pattern_t = transposed(pattern)
    for i in range(0, len(pattern_t)-1):
        if is_mirrored(pattern_t, i):
            total += (i+1)

print('Part1', total)

# Going to try the dumb way

patterns = [[list(line) for line in pattern] for pattern in patterns]

def pattern_score(pattern):
    total = 0
    y_folds = []
    x_folds = []
    for i in range(0, len(pattern)-1):
        if is_mirrored(pattern, i):
            y_folds.append(i)
            total += 100 * (i+1)
    pattern_t = transposed(pattern)
    for i in range(0, len(pattern_t)-1):
        if is_mirrored(pattern_t, i):
            x_folds.append(i)
            total += (i+1)

    return total, y_folds, x_folds

grand_total = 0
for pattern in patterns:
    total, y_folds, x_folds = pattern_score(pattern)
    ref_y = set(y_folds)
    ref_x = set(x_folds)

    for j,i in ((j,i) for i in range(len(pattern[0])) for j in range(len(pattern))):
        pattern[j][i] = '.' if pattern[j][i] == '#' else '#'
        total, y_folds, x_folds = pattern_score(pattern)
        pattern[j][i] = '.' if pattern[j][i] == '#' else '#'
        if total > 0:
            if any((y not in ref_y) for y in y_folds) or any((x not in ref_x) for x in x_folds):
                new_ys = [y for y in y_folds if y not in ref_y]
                new_xs = [x for x in x_folds if x not in ref_x]
                total = 0
                for y in new_ys:
                    total += 100 * (y+1)
                for x in new_xs:
                    total += (x+1)
                grand_total += total
                break

print('Part2', grand_total)