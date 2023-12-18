from itertools import cycle
import euclid
from math import lcm

with open('input.txt', 'r') as file:
    lines = file.readlines()

directions = lines[0].strip()
map = {line[0:3]:(line[7:10], line[12:15]) for line  in lines[2:]}

# Part 1

state = 'AAA'
moves = 0
for d in cycle(directions):
    if state == 'ZZZ':
        break
    if d == 'L':
        state = map[state][0]
    else:
        state = map[state][1]
    moves += 1
    
print('Part1', moves)

# Part 2
starts = []
for key,value in map.items():
    if key[-1] == 'A':
        starts.append(key)

paths = []
for start in starts:
    state = start
    mode = 0
    phase = 0
    period = 0
    moves = 0
    for d in cycle(directions):
        if state[-1] == 'Z':
            if mode == 0:
                phase = moves
                moves = 0
                mode = 1
            else:
                period = moves
                break
        lr = 0 if d == 'L' else 1
        state = map[state][lr]
        moves += 1
    paths.append((phase, period))       

print('Part2', lcm(*[path[0] for path in paths]))