def main():
    with open('input') as f:
        matches = [''.join(l.split()) for l in f.readlines()]

    score = 0
    for matchup in matches:
        if matchup[1] == 'X':
            score += 1
        elif matchup[1] == 'Y':
            score += 2
        elif matchup[1] == 'Z':
            score += 3

        if 'ABC'.index(matchup[0]) == 'XYZ'.index(matchup[1]):
            score += 3
        elif matchup in ['AY', 'BZ', 'CX']:
            score += 6
        elif matchup in ['AZ', 'BX', 'CY']:
            score += 0

    print(score)

    score = 0
    for matchup in matches:
        if matchup[1] == 'X':
            score += 0
        elif matchup[1] == 'Y':
            score += 3
        elif matchup [1] == 'Z':
            score += 6

        if matchup in ['AY', 'BX', 'CZ']:
            score += 1
        elif matchup in ['BY', 'AZ', 'CX']:
            score += 2
        elif matchup in ['CY', 'AX', 'BZ']:
            score += 3

    print(score)

if __name__ == '__main__':
    main()
