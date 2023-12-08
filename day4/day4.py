with open('input.txt', 'r') as file:
    lines = file.readlines()

lines = [line[line.find(':')+1:] for line in lines]

# Part 1
total = 0
for line in lines:
    lhs, rhs = line.split('|')
    lnums = set(int(x) for x in lhs.strip().split())
    rnums = [int(x) for x in rhs.strip().split()]
    rnums_in = [x for x in rnums if x in lnums]
    count = len(rnums_in)
    if count > 0:
        total += 2**(count-1)

print('Part 1', total)

# Part 2
copies = {i:1 for i in range(len(lines))}
total = 0
for i, line in enumerate(lines):
    lhs, rhs = line.split('|')
    lnums = set(int(x) for x in lhs.strip().split())
    rnums = [int(x) for x in rhs.strip().split()]
    rnums_in = [x for x in rnums if x in lnums]
    count = len(rnums_in)
    
    for j in range(count):
        k = i+1+j
        if k >= len(lines):
            break
        copies[i+1+j] += copies[i]

    total += copies[i]

print('Part 2', total)