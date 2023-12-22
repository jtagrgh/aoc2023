with open('input.txt', 'r') as file:
    steps = file.read().strip().split(',')

def hash(label):
    total = 0
    for c in label:
        total += ord(c)
        total *= 17
        total %= 256
    return total

print('Part1', sum(hash(step) for step in steps))

boxes = [[0,{}] for _ in range(256)]
for step in steps:
    if step[-1] == '-':
        label = step[0:-1]
        box_num = hash(label)
        if label in boxes[box_num][1]:
            del boxes[box_num][1][label]
    else:
        label, focal = step.split('=')
        focal = int(focal)
        box_num = hash(label)
        if label in boxes[box_num][1]:
            boxes[box_num][1][label][0] = focal
        else:
            boxes[box_num][1][label] = [focal, boxes[box_num][0]]
            boxes[box_num][0] += 1

total = 0
for bn, box in enumerate(boxes):
    if len(box[1]) < 1:
        continue
    lenses = [(order, focal) for focal,order in box[1].values()]
    lenses = sorted(lenses)
    for sn, lens in enumerate(lenses):
        total += (bn+1) * (sn+1) * lens[1]

print('Part2', total)