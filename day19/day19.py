import re
from math import prod

with open('input.txt', 'r') as file:
    sections = file.read().split('\n\n')
    workflows = sections[0].splitlines()
    parts = sections[1].splitlines()

p = re.compile(r'(\D+)\{(.*)\}')
workflow_map = {}
for line in workflows:
    name, spec = p.match(line).groups()
    rules = spec.split(',')
    rules = [rule.split(':') for rule in rules]
    parsed_rules = []
    for rule in rules:
        if len(rule) > 1:
            parsed_rules.append((rule[0], rule[1]))
        else:
            parsed_rules.append(('True', rule[0]))
    workflow_map[name] = parsed_rules

parts = [part[1:-1].split(',') for part in parts]

end_state = {'A':[], 'R':[]}

for part in parts:
    wf = 'in'
    for rating in part:
        exec(rating)
    while wf not in ('A', 'R'):
        for pred, nwf in workflow_map[wf]:
            if eval(pred):
                wf = nwf
                break
    end_state[wf].append(part)

total = 0
for acc_part in end_state['A']:
    for rating in acc_part:
        exec(rating)
    total += x + m + a + s

print('Part1', total)


var_index = {'x':0, 'm':1, 'a':2, 's':3}
end_state = {'A':[], 'R':[]}
stack = [('in',((1,4000),(1,4000),(1,4000),(1,4000)))]
while len(stack) > 0:
    ins = stack.pop()
    part = ins[1]
    key = ins[0]
    if any(rating[0] > rating[1] for rating in part):
        continue
    if key in ('A', 'R'):
        end_state[key].append(part)
        continue
    wf = workflow_map[key]
    for pred, nwf in wf:
        if len(pred_split := pred.split('<')) == 2:
            var, val = pred_split
            val = int(val)
            vari = var_index[var]
            val -= 1
            if val >= part[vari][0]:
                new_ratings = [rating for rating in part]
                new_part_ratings = [rating for rating in part]
                new_ratings[vari] = (part[vari][0], min(val, part[vari][1]))
                new_part_ratings[vari] = (val+1, part[vari][1])
                stack.append((nwf, tuple(new_ratings)))
                part = tuple(new_part_ratings)
        elif len(pred_split := pred.split('>')) == 2:
            var, val = pred_split
            val = int(val)
            vari = var_index[var]
            val += 1
            if val <= part[vari][1]:
                new_ratings = [rating for rating in part]
                new_part_ratings = [rating for rating in part]
                new_ratings[vari] = (max(val, part[vari][0]), part[vari][1])
                new_part_ratings[vari] = (part[vari][0], val-1)
                stack.append((nwf, tuple(new_ratings)))
                part = tuple(new_part_ratings)
        else:
            stack.append((nwf, part))

total = 0
for part in end_state['A']:
    total += prod(rating[1] - rating[0] + 1 for rating in part)

print('Part2', total)