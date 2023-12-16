from collections import Counter

with open('input.txt', 'r') as file:
    lines = file.readlines()

hand_types = {k:i for i,k in enumerate([(1,1,1,1,1), (2,1,1,1), (2,2,1), (3,1,1), (3,2), (4,1), (5,)])}
card_values = {k:i for i,k in enumerate(['2','3','4','5','6','7','8','9','T','J','Q','K','A'])}

data = [line.strip().split() for line in lines]

# Part 1
def cmp_key(elem):
    freqs = sorted([x[1] for x in Counter(elem[0]).items()], reverse=True)
    cards = [card_values[x] for x in elem[0]]
    return (hand_types[tuple(freqs)], cards)

data = sorted(data, key=cmp_key)

total = 0
for i, elem in enumerate(data):
    total += int(elem[1]) * (i+1)

print('Part1', total)

# Part 2
card_values = {k:i for i,k in enumerate(['J','2','3','4','5','6','7','8','9','T','Q','K','A'])}

def cmp_key2(elem):
    counts = Counter(elem[0])
    freqs = sorted([x[1] for x in counts.items()], reverse=True)
    cards = [card_values[x] for x in elem[0]]
    rank = hand_types[tuple(freqs)]
    if 'J' in counts.keys():
        if rank == 0:
            rank += 1
        elif rank == 1:
            rank += 2
        elif rank == 2:
            if counts['J'] == 1:
                rank += 2
            elif counts['J'] == 2:
                rank += 3
        elif rank == 3:
            rank += 2
        elif rank == 4:
            rank += 2
        elif rank == 5:
            rank += 1
    return (rank, cards)

data = sorted(data, key=cmp_key2)

total = 0
for i, elem in enumerate(data):
    total += int(elem[1]) * (i+1)

print('Part2', total)