with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

lines.insert(0, ''.join(['#' for _ in lines[0]]))

total = 0
for j in range(len(lines)):
    for i in range(len(lines[0])):
        if lines[j][i] == 'O':
            length = 0
            n_rollers = 0
            for k in range(j):
                length += 1
                match lines[j-k-1][i]:
                    case 'O':
                        n_rollers += 1
                    case '#':
                        break
            roll_y_pos = j - length + 1 + n_rollers
            total += len(lines) - roll_y_pos

print('Part1', total)

lines = ['#' + line + '#' for line in lines]
lines.append(''.join(['#' for _ in lines[0]]))
lines = [list(line) for line in lines]

def wested(matrix):
    return [list(l) for l in zip(*matrix)]

def southed(matrix):
    return reversed(matrix)

def easted(matrix):
    return wested([reversed(l) for l in matrix])

def x_flip(matrix):
    return [list(reversed(row)) for row in matrix]

def roll_north(lines):
    for j in range(len(lines)):
        for i in range(len(lines[0])):
            if lines[j][i] == 'O':
                length = 0
                n_rollers = 0
                for k in range(j):
                    length += 1
                    match lines[j-k-1][i]:
                        case 'O':
                            n_rollers += 1
                        case '#':
                            break
                roll_y_pos = j - length + 1 + n_rollers
                lines[j][i] = '.'
                lines[roll_y_pos][i] = 'O'
    return lines

def cycled(matrix):
    return x_flip(easted(roll_north(easted(roll_north(easted(roll_north(wested(roll_north([row[:] for row in matrix])))))))))

def roller_positions(matrix):
    positions = []
    for j in range(len(matrix)):
        for i in range(len(matrix[0])):
            if matrix[j][i] == 'O':
                positions.append((j,i))
    return positions

def load(matrix):
    total = 0
    for j in range(len(matrix)):
        for i in range(len(matrix[0])):
            if matrix[j][i] == 'O':
                total += len(matrix) - j - 1
    return total

results = []
results_matrixes = []
cycle_start = 0
for _ in range(1000000000):
    lines = cycled(lines)
    rollers = tuple(roller_positions(lines))
    if rollers in results:
        cycle_start = results.index(rollers)
        break
    results.append(rollers)
    results_matrixes.append(lines)

left = 1000000000 - cycle_start - 1
cycle_length = len(results) - cycle_start
gap = left % cycle_length
total = load(results_matrixes[gap + cycle_start])

print('Part2', total)