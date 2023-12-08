with open('input.txt', 'r') as file:
    lines = [line.rstrip() for line in file.readlines()]

# Part 1
def is_symbol(c):
    return not c.isnumeric() and c != '.'

nn = len(lines[0])
mm = len(lines)

state = 0
num = 0
total = 0
is_adj = False

for m in range(mm):
    for n in range(nn):
        x = lines[m][n]

        if x.isnumeric() and not is_adj:
            for i in (-1, 0, 1):
                cn = n + i
                if cn < 0 or cn >= nn:
                    continue
                for j in (-1, 0, 1):
                    cm = m + j
                    if cm < 0 or cm >= mm:
                        continue
                    if is_symbol(lines[cm][cn]):
                        is_adj = True
                        break

        if state == 0:
            if x.isnumeric():
                num += int(x)
                state = 1
            elif x != '.':
                pass
        else:
            if x.isnumeric():
                num *= 10
                num += int(x)
            else:
                state = 0
                if is_adj:
                    total += num
                is_adj = False
                num = 0

print('Part 1', total)

from collections import deque

# Part 2
total = 0
coords = ((j,i) for j in range(mm) for i in range(nn))

for j,i in coords:
    x = lines[j][i]
    if x != '*':
        continue

    to_check = [(i+k,j+l) for k in (-1, 0, 1) for l in (-1, 0, 1)]
    to_check = [x for x in to_check if x[0] >= 0 and x[0] < nn]
    to_check = [x for x in to_check if x[1] >= 0 and x[1] < mm]
    check_set = set(to_check)

    prod = 1
    n_found = 0
    
    for k,l in to_check:
        if (k,l) not in check_set:
            continue
        y = lines[l][k]
        if not y.isnumeric():
            continue
        check_set.discard((k,l))
        digits = deque()
        digits.append(int(y))
        r = k+1
        while r < nn and lines[l][r].isnumeric():
            digits.append(int(lines[l][r]))
            check_set.discard((r,l))
            r += 1
        r = k-1
        while r >= 0 and lines[l][r].isnumeric():
            digits.appendleft(int(lines[l][r]))
            check_set.discard((r,l))
            r -= 1
        
        n_found += 1
        num = 0
        for digit in digits:
            num *= 10
            num += digit
        prod *= num

    if n_found == 2:
        total += prod

print('Part 2', total)