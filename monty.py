from random import shuffle, randint

def get_doors(n):
    doors = ['car']
    for i in range(n-1):
        doors.append('goat')
    shuffle(doors)
    return doors


def monty(stay=True):
    num_doors = 3
    doors = get_doors(num_doors)

    user_choice_index = randint(0, num_doors-1)
    user_choice = doors.pop( user_choice_index )

    # Removes first goat
    doors.remove('goat')
    remain_choice = doors.pop()

    if stay:
        return user_choice=='car'
    return remain_choice=='car'

def main():
    cycles = 100000
    stay_wins   = 0
    change_wins = 0
    for i in range(cycles):
        stay_wins   += monty()
    for i in range(cycles):
        change_wins += monty(False)

    percent_stay_wins = stay_wins*1.0/cycles
    percent_change_wins = change_wins*1.0/cycles
    print 'number of cycles:    {} cycles'.format(cycles)
    print 'percent_stay_wins:   {}%'.format(percent_stay_wins)
    print 'percent_change_wins: {}%'.format(percent_change_wins)

if __name__ == '__main__':
    main()
