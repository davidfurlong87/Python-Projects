from random import shuffle, randint


def number_checker(message):
    print(message)
    try:
        number = eval(input())
        if 5 >= number >= 1:
            return int(number)
        else:
            raise Exception
    except:
        random_choice = randint(1,5)
        print("A mistake. Let's set that to %d for you" % (random_choice))
        print()
        return random_choice


def print_grid():
    for r in n:
        print(r)
    print(' - ' * 20)


def new_game():
    characters = ['@', 5, '#', 'A', '!', 0, 'b', '$', 'z', 'N', 'x', '-', '+', ':', 'c'] * 2
    shuffle(characters)
    global m
    global n
    m = [[characters[c + r] for c in range(6)] for r in range(0, 30, 6)]
    n = [['*' for c in range(6)] for r in range(5)]
    rem = 30
    while rem > 0:
        print_grid()
        x1 = number_checker('Please enter the row of the first character:')
        y1 = number_checker('Please enter the column of the first character:')
        n[x1 - 1][y1 - 1] = m[x1 - 1][y1 - 1]
        print_grid()
        x2 = number_checker('Please enter the row of the second character:')
        y2 = number_checker('Please enter the column of the second character:')
        n[x2 - 1][y2 - 1] = m[x2 - 1][y2 - 1]
        print_grid()
        if n[x1 - 1][y1 - 1] != n[x2 - 1][y2 - 1] or (x1 == x2 and y1 == y2):
            n[x1 - 1][y1 - 1] = '*'
            n[x2 - 1][y2 - 1] = '*'
        else:
            rem = rem - 2
            print(f'''
    There are {rem} cells remaining
    ''')
    print('''
    You win!''')


def main():
    new_game()


def cont():
    print("""
Play again?

Press 'Y' for Yes or anything else for No""")
    x = input()
    if x.upper() == "Y":
        return True
    else:
        return False


run = True
while run:
    main()
    run = cont()
