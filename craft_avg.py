import sys
import random


def xd6(x, multiplier):
    #print('%d %d' % (x, multiplier))
    return sum([random.randint(1,6) for x in range(x)]) * multiplier

def get_event_dc():
    d20a = random.randint(1,20)
    #print('d20a %d' % (d20a))
    if d20a <= 4:
        return { 'cr':'0', 'dc':8, 'xp':10, 'reward': [2, 1] }
    elif d20a <= 8:
        return { 'cr':'1/8', 'dc':9, 'xp':25, 'reward': [2, 5] }
    elif d20a <= 12:
        return { 'cr':'1/4', 'dc':10, 'xp':50, 'reward': [4, 1] }
    elif d20a <= 16:
        return { 'cr':'1/2', 'dc':12, 'xp':100, 'reward': [2, 10] }
    elif d20a <= 19:
        return { 'cr':'1', 'dc':15, 'xp':200, 'reward': [3, 10] }
    else:
        d20b = random.randint(1,20)
        #print('d20b %d' % (d20b))
        if d20b <= 10:
            return { 'cr':'2', 'dc':18, 'xp':450, 'reward': [4, 10] }
        elif d20b <= 14:
            return { 'cr':'3', 'dc':21, 'xp':700, 'reward': [2, 50] }
        elif d20b <= 17:
            return { 'cr':'4', 'dc':24, 'xp':1100, 'reward': [2, 100] }
        elif d20b <= 19:
            return { 'cr':'5', 'dc':27, 'xp':1800, 'reward': [3, 100] }
        else:
            return { 'cr':'6', 'dc':30, 'xp':2500, 'reward': [4, 100] }
    assert False

def is_event_month():
    z = random.randint(1,6)
    if z < 5:
        return True
    return False

_TRADECRAFT_EVENTS = {
1: 'STR check',
2: 'DEX check',
3: 'CON check',
4: 'INT check',
5: 'INT check',
6: 'WIS check',
7: 'WIS check',
8: 'CHA check',
9: 'CHA check',
10: 'Athletics (STR)',
11: 'Arcana (INT)',
12: 'History (INT)',
13: 'Investigation (INT)',
14: 'Investigation (INT)',
15: 'Nature (INT)',
16: 'Religion (INT)',
17: 'Animal Handling (WIS)',
18: 'Animal Handling (WIS)',
19: 'Insight (WIS)',
20: 'Insight (WIS)',
21: 'Medicine (WIS)',
22: 'Perception (WIS)',
23: 'Perception (WIS)',
24: 'Survival (WIS)',
25: 'Deception (CHA)',
26: 'Intimidation (CHA)',
27: 'Performance (CHA)',
28: 'Persuasion (CHA)',
29: 'Persuasion (CHA)',
30: 'Monster Encounter'
}

def place_roll(hist, roll, points):
    for point in points:
        if roll >= point:
            hist[point] += 1
            return
    assert False, ('hist %s, roll %d, points %s') % (hist, roll, points)

def roll_to_points(roll):
    if roll < 15:
        return 0
    elif roll < 20:
        return 1
    elif roll < 25:
        return 2
    elif roll < 30:
        return 3
    elif roll < 35:
        return 4
    elif roll < 40:
        return 5
    elif roll < 45:
        return 6
    elif roll < 50:
        return 7
    elif roll < 55:
        return 8

def main(args):
    days = int(args[0])
    attempts_per_roll = int(args[1])
    rolls_per_day = int(args[2])
    mod = int(args[3])

    print('%d\t%d\t%d\t%d' % (days, attempts_per_roll, rolls_per_day, mod))

    points = 0
    total_rolls = days * rolls_per_day
    for tt in range(total_rolls):
        roll = max([random.randint(1,20)+mod for x in range(attempts_per_roll)])
        points += roll_to_points(roll)

    avg = 1.0 * points / days
    print('points %d, avg %f' % (points, avg))

if __name__ == '__main__':
    main(sys.argv[1:])
