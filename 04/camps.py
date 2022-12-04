def main():
    with open('input') as f:
        camps = [l.strip().split(',') for l in f.readlines()]

    contained = 0

    for c in camps:
        c1, c2 = c
        if (int(c1.split('-')[0]) <= int(c2.split('-')[0])
                and int(c1.split('-')[1]) >= int(c2.split('-')[1])):
            contained += 1
        elif (int(c1.split('-')[0]) >= int(c2.split('-')[0])
                and int(c1.split('-')[1]) <= int(c2.split('-')[1])):
            contained += 1

    print(contained)

    partially = 0

    for c in camps:
        c1, c2 = c
        if (int(c1.split('-')[0]) <= int(c2.split('-')[1])
            and int(c1.split('-')[1]) >= int(c2.split('-')[0])):
            partially += 1

    print(partially)

if __name__ == '__main__':
    main()
