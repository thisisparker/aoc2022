import string

def main():

    with open('input') as f:
        sacks = [l.strip() for l in f.readlines()]

    priority_list = '_' + string.ascii_letters
    priority_sum = 0

    for s in sacks:
        mispack = set(s[:len(s)//2]).intersection(set(s[len(s)//2:])).pop()
        priority_sum += priority_list.index(mispack)

    print(priority_sum)

    badge_sum = 0
    
    for g in range(0, len(sacks), 3):
        group = sacks[g:g+2]
        badge = set(sacks[g]).intersection(set(sacks[g+1])).intersection(
                set(sacks[g+2])).pop()

        badge_sum += priority_list.index(badge)

    print(badge_sum)

if __name__ == '__main__':
    main()
