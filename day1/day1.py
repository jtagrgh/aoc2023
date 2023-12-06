with open('input.txt', 'r') as f:
    lines = f.readlines()

# Part 1
sum = 0
for line in lines:
    first_digit = 0
    last_digit = 0
    for char in line:
        if char.isdigit():
            first_digit = int(char)
            break
    for char in reversed(line):
        if char.isdigit():
            last_digit = int(char)
            break

    sum += first_digit*10 + last_digit
print('Part 1', sum)

# Part 2
word_nums = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
digi_nums = ('1', '2', '3', '4', '5', '6', '7', '8', '9')

sum = 0

for line in lines:
    fi = len(line)
    fn = -1

    for l in (word_nums, digi_nums):
        for i, wn in enumerate(l):
            at = line.find(wn)
            if at != -1 and at < fi:
                fn = i + 1
                fi = at

    li = -1
    ln = -1

    for l in (word_nums, digi_nums):
        for i, wn in enumerate(l):
            at = line.rfind(wn)
            if at != -1 and at > li:
                ln = i + 1
                li = at

    sum += fn * 10 + ln

print('Part 2', sum)