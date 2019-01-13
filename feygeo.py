import sys
import random
import math
import dlib

_doms = [
    'Arcana',
    'Ambition',
    'Death',
    'Forge',
    'Grave',
    'Knowledge',
    'Life',
    'Light',
    'Nature',
    'Solidarity',
    'Strength',
    'Tempest',
    'Trickery',
    'War',
    'Zeal',
]

zz = """
Azurite\tblue
Banded Agate\tpurple
Blue Quartz\tblue
Eye agate\twhite
Hematite\tblack
Lapis lazuli\tblue
Malachite\tgreen
Moss agate\tgold silver
Obsidian\tblack
Rhodochrosite\tred
Tiger eye\tgold
Turquoise\tgreen
Bloodstone\tred
Carnelian\torange
Chalcedony\twhite
Chrysoprase\tgreen
Citrine\tgold
Jasper\tblack
Moonstone\tsilver Blue
Onyx\tblack
Quartz\tsilver
Sardonyx\tred
Star rose quartz\tred silver
Zircon\tblue green
100 Pearl\tsilver gold red
500 Black\tpearl black
"""

numer = {
    'l': 1, 's': 2, 'k': 3, 'b': 4, 'z': 5, 'f': 6, 'u': 7,
    'x': 8, 'q': 9, 'y': 10, 'p': 11, 'h': 12, 'e': 13,
    't': 14, 'r': 15, 'm': 16, 'j': 17, 'i': 18, 'd': 19,
    'a': 20, 'o': 21, 'w': 22, 'n': 23, 'c': 24, 'v': 25, 'g': 26\
}

qq = [
'A	20',
'B	4',
'C	24',
'D	19',
'E	13',
'F	6',
'G	26',
'H	12',
'I	18',
'J	17',
'K	3',
'L	1',
'M	16',
'N	23',
'O	21',
'P	11',
'Q	9',
'R	15',
'S	2',
'T	14',
'U	7',
'V	25',
'W	22',
'X	8',
'Y	10',
'Z	5',
]

def main(args):
    #print(args)

    #p = 'abcdefghijklmnopqrstuvwxyz'
    #print(len(p))
    #ss = zip(dlib.scramble([p[x] for x in range(len(p))]),[x+1 for x in range(len(p))])
    #print(ss)
    #dd = dict(ss)
    #print(dd)
    #kk = list(dd.keys())
    #kk.sort()
    #print('\n'.join(['%s\t%d' % (k.upper(),dd[k]) for k in kk]))
    #print(dlib.scramble(args))
    #print('\n'.join(dlib.scramble(args)))

    #qq2 = dlib.scramble(qq)
    #print('\n'.join(qq2))
    for arg in args:
        if arg == '?':
            print(numer)
            k2 = list(numer.keys())
            k2.sort()
            print(', '.join(['%s: %d' % (k, numer[k]) for k in k2]))

        else:
            print(arg)
            ss = [x for x in arg]
            print(ss)
            vv= [numer[x] for x in ss]
            print(vv)
            tot = sum(vv)
            div = 1.0 * tot / 28
            rem = tot % 28
            print('sum %d, div %f, rem %d' %(tot, div, rem))

        print('')

if __name__ == '__main__':
    main(sys.argv[1:])
