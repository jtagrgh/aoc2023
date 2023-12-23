with open('input.txt', 'r') as file:
    grid = file.read().splitlines()

up, down, left, right = (-1,0), (1,0), (0,-1), (0,1)

def count_energized(start):
    beams = [start]
    energized = set()
    hit = set()

    while len(beams) > 0:
        beam = beams.pop()
        pos, dir = beam
        energized.add(pos)

        if beam in hit:
            continue
        else:
            hit.add(beam)

        next_pos = (pos[0] + dir[0], pos[1] + dir[1])
        if next_pos[0] >= len(grid) or next_pos[0] < 0:
            continue
        if next_pos[1] >= len(grid[0]) or next_pos[1] < 0:
            continue

        match grid[next_pos[0]][next_pos[1]]:
            case '.':
                beams.append((next_pos, dir))
            case '|':
                if dir in (right, left):
                    beams.append((next_pos, up))
                    beams.append((next_pos, down))
                else:
                    beams.append((next_pos, dir))
            case '-':
                if dir in (up, down):
                    beams.append((next_pos, left))
                    beams.append((next_pos, right))
                else:
                    beams.append((next_pos, dir))
            case '/':
                if dir == up:
                    beams.append((next_pos, right))
                elif dir == down: 
                    beams.append((next_pos, left))
                elif dir == left:
                    beams.append((next_pos, down))
                elif dir == right:
                    beams.append((next_pos, up))
            case '\\':
                if dir == up:
                    beams.append((next_pos, left))
                elif dir == down: 
                    beams.append((next_pos, right))
                elif dir == left:
                    beams.append((next_pos, up))
                elif dir == right:
                    beams.append((next_pos, down))
    return len(energized) - 1
            
print('Part1', count_energized(((0,-1), right)))

starts = [((-1,x), down) for x in range(len(grid[0]))]
starts.extend(((len(grid),x), up) for x in range(len(grid[0])))
starts.extend(((y,-1), right) for y in range(len(grid)))
starts.extend(((y,len(grid[0])), left) for y in range(len(grid)))

most_energized = -float('inf')
for start in starts:
    most_energized = max(most_energized, count_energized(start))

print('Part2', most_energized)