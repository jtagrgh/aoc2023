with open('input.txt', 'r') as file:
    lines = file.readlines()

seeds = [int(x) for x in lines[0][6:].strip().split()]
maps = [[]]

for line in lines[2:]:
    if line == '\n':
        maps.append([])
    line = line.strip().split()
    if len(line) != 0 and line[0].isnumeric():
        maps[-1].append(tuple(int(x) for x in line))

# Part 1
lowest = float('inf')
for seed in seeds:
    for map in maps:
        for interval in map:
            if seed >= interval[1] and seed <= interval[1] + interval[2]:
                seed = seed + (interval[0] - interval[1])
                break
    lowest = min(lowest, seed)
print(lowest)

# Part 2
intervals = list(zip(seeds[0::2], seeds[1::2]))
intervals = [(s,s+l) for s,l in intervals]

for map in maps:
    new_intervals = []
    for interval in intervals:
        working_set = set()
        working_set.add(interval)
        for filter in map:
            working_set_copy = list(working_set)
            mod = filter[0] - filter[1]
            f_start = filter[1]
            f_end = filter[1] + filter[2] - 1
            exploded_pieces = []
            for piece in working_set_copy:
                if (f_end < piece[0] or f_start > piece[1]):
                    continue
                filtered = (max(f_start, piece[0]), min(f_end, piece[1]))
                new_intervals.append((filtered[0] + mod, filtered[1] + mod))
                working_set.remove(piece)
                if filtered[0] > piece[0]:
                    exploded_pieces.append((piece[0], filtered[0] - 1))
                if filtered[1] < piece[1]:
                    exploded_pieces.append((filtered[1] + 1, piece[1]))

            for exploded_piece in exploded_pieces:
                working_set.add(exploded_piece)

        new_intervals += list(working_set)

    intervals = new_intervals

print(min((i[0] for i in intervals)))

# print(intervals)