def get_line():
    with open('input.txt', 'r') as file:
        for line in file:
            yield line

# Part 1
out = 0
for i, round in enumerate(get_line()):
    games = round[round.find(':')+1:].split(';')

    def valid_game(game):
        counts = {'red':0, 'green':0, 'blue':0}
        hands = game.split(',')
        for hand in hands:
            draw = hand.strip().split(' ')
            counts[draw[1]] += int(draw[0])
        return counts['red'] <= 12 and counts['green'] <= 13 and counts['blue'] <= 14

    if all(valid_game(game) for game in games):
        out += i + 1
print('Part 1', out)

# Part 2
out = 0
for i, round in enumerate(get_line()):
    round_counts = {'red':0, 'green':0, 'blue':0}
    games = round[round.find(':')+1:].split(';')
    for game in games:
        game_counts = {'red':0, 'green':0, 'blue':0}
        for hand in game.split(','):
            draw = hand.strip().split()
            game_counts[draw[1]] += int(draw[0])
        for colour, count in game_counts.items():
            if count > round_counts[colour]:
                round_counts[colour] = count
    round_power = 1
    for count in round_counts.values():
        round_power *= count
    out += round_power
print('Part 2', out)