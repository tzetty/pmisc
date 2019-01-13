import sys
import random

def show_roll(text):
    pp = text.split('d')
    assert len(pp) == 2
    if len(pp[0]) > 0:
        die_count = int(pp[0])
    else:
        die_count = 1

    plus_pos = pp[1].find('+')
    minus_pos = pp[1].find('-')
    if plus_pos != -1:
        die_size = int(pp[1][:plus_pos])
        suffix = int(pp[1][plus_pos:])
    elif minus_pos != -1:
        die_size = int(pp[1][:minus_pos])
        suffix = int(pp[1][minus_pos:])
    else:
        die_size = int(pp[1])
        suffix = 0

    rolls = [random.randint(1,die_size) for x in range(die_count)]
    total = sum(rolls) + suffix

    print("%s: %s %d = %d" % (text, rolls, suffix, total))

def main(args):
    for arg in args:
        show_roll(arg)

if __name__ == '__main__':
    main(sys.argv[1:])
