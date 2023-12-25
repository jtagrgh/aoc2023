with open('input.txt', 'r') as file:
    lines = [line.split() for line in file.read().splitlines()]
    lines = [[a,int(b),c] for a,b,c in lines]

dir_map = {'U':0+1j, 'D':0-1j, 'L':-1+0j, 'R':1+0j}
positions = [0+0j]
for line in lines:
    for b in range(line[1]):
        positions.append(positions[-1] + dir_map[line[0]])

positions.pop()

area = 0
for i, p in enumerate(positions):
    area += p.real * (p - positions[i-1]).imag
area = int(abs(area))
n_inter_points = int(area - len(positions)/2 + 1)
border_area = sum(d for _,d,_ in lines)
total_trench = n_inter_points + border_area

print('Part1', total_trench)

# Below is the better way to do this, O(n) time O(1) space
dir_map = {0:1+0j, 1:0-1j, 2:-1+0j, 3:0+1j}
area = 0
pos = 0+0j
n_pos = 0
for line in lines:
    ins = line[2][2:-1]
    dist = int(ins[0:5], 16)
    dir = dir_map[int(ins[-1], 16)]
    
    new_pos = pos + (dir * dist)
    area += new_pos.real * (new_pos - pos).imag
    pos = new_pos
    n_pos += dist

n_inter_points = int(abs(area) - n_pos/2 + 1)
print('Part2', n_inter_points + n_pos)