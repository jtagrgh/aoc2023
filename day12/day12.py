with open('input.txt', 'r') as file:
    lines = [line.split() for line in file.read().splitlines()]
    for line in lines:
        line[0] = list(line[0])
        line[1] = [int(x) for x in line[1].split(',')]

def place(to_place, i, line, start):
    if i == len(to_place):
            return not any(x == '#' for x in line)

    count = 0

    for j, c in enumerate(line[start:], start):
        if c in ('.', 'x'): 
            continue

        ahead = 0

        for h in line[j:]:
            if h in ('.', 'x'): 
                break
            else: 
                ahead += 1

        if ahead < to_place[i]:
            continue

        line_copy = line.copy()

        for k in range(j, j + to_place[i]):
            line_copy[k] = 'x'

        count += place(to_place, i+1, line_copy, j+to_place[i]+1)

    return count

total = sum(place(line[1], 0, line[0], 0) for line in lines)
print('Part1', total)

def place2(mem, to_place, i, line):
    key = (i, len(line))

    if key in mem:
        return mem[key]

    if i == len(to_place):
        good = not any(x == '#' for x in line)
        return good

    count = 0

    last = False

    for j, c in enumerate(line):
        if last:
            break

        if c == '#':
            last = True

        if c == '.': 
            continue

        ahead = 0
        for h in line[j:]:
            if h == '.': 
                break
            ahead += 1
        if ahead < to_place[i]:
            continue

        if j+to_place[i] < len(line) and line[j+to_place[i]] == '#':
            continue

        count += place2(mem, to_place, i+1, line[j+to_place[i]+1:])

    mem[key] = count
    return count

# Do not write this
lines2 = [('?'.join(''.join(line[0]) for _ in range(5)), line[1]*5) for line in lines]
total = sum(place2(dict(), line[1], 0, line[0]) for line in lines2)

print('Part2', total)