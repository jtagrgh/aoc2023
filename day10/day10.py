with open('input.txt', 'r') as file:
    lines = file.readlines()

lines = ['.' + line.strip() + '.' for line in lines]
dots = '.' * len(lines[0])
lines.insert(0, dots)
lines.append(dots)

n = len(lines[0])
m = len(lines)

s = None
for j in range(m):
    for i in range(n):
        if lines[j][i] == 'S':
            s = (j,i)
            break

def up(pair):
    return (pair[0]-1, pair[1])

def down(pair):
    return (pair[0]+1, pair[1])

def left(pair):
    return (pair[0], pair[1]-1)

def right(pair):
    return (pair[0], pair[1]+1)

def at2(self, pair):
    return self[pair[0]][pair[1]]

connected_to_s = []
if at2(lines, up(s)) in ('|', '7', 'F'):
    connected_to_s.append(up(s))
if at2(lines, right(s)) in ('-', '7', 'J'):
    connected_to_s.append(right(s))
if at2(lines, down(s)) in ('|', 'J', 'L'):
    connected_to_s.append(down(s))
if at2(lines, left(s)) in ('-', 'L', 'F'):
    connected_to_s.append(left(s))

p = connected_to_s[0]
old_p = s
q = connected_to_s[1]
old_q = s

steps = 1
while p != q:
    value = lines[p[0]][p[1]]

    match value:
        case '|':
            possibles = [up(p), down(p)]
        case '-':
            possibles = [left(p), right(p)]
        case 'L':
            possibles = [up(p), right(p)]
        case 'J':
            possibles = [up(p), left(p)]
        case '7':
            possibles = [left(p), down(p)]
        case 'F':
            possibles = [down(p), right(p)]

    possibles = [p for p in possibles if p != old_p]
    old_p = p
    p = possibles[0]

    value = lines[q[0]][q[1]]
    match value:
        case '|':
            possibles = [up(q), down(q)]
        case '-':
            possibles = [left(q), right(q)]
        case 'L':
            possibles = [up(q), right(q)]
        case 'J':
            possibles = [up(q), left(q)]
        case '7':
            possibles = [left(q), down(q)]
        case 'F':
            possibles = [down(q), right(q)]

    possibles = [q for q in possibles if q != old_q]
    old_q = q
    q = possibles[0]

    steps += 1

print('Part1', steps)

points = [s]

p = connected_to_s[0]
old_p = s
while p != s:
    points.append(p)
    value = lines[p[0]][p[1]]

    match value:
        case '|':
            possibles = [up(p), down(p)]
        case '-':
            possibles = [left(p), right(p)]
        case 'L':
            possibles = [up(p), right(p)]
        case 'J':
            possibles = [up(p), left(p)]
        case '7':
            possibles = [left(p), down(p)]
        case 'F':
            possibles = [down(p), right(p)]

    possibles = [p for p in possibles if p != old_p]
    old_p = p
    p = possibles[0]

area = 0
for i, p in enumerate(points):
    area += p[1] * (p[0] - points[i-1][0])

interior_points = int(abs(area) - len(points)/2 + 1)

print('Part2', interior_points)