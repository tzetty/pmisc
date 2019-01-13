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
    '?',
    '?',
    '?',
    '?',
    '?',
    '?',
    '?',
    '?',
    '?',
    '?',
    '?',
    '?'
]

zz = """
Azurite blue
Banded Agate purple
Blue Quartz blue
Eye agate white
Hematite black
Lapis lazuli blue
Malachite green
Moss agate gold silver
Obsidian black
Rhodochrosite red
Tiger eye gold
Turquoise green

Bloodstone red
Carnelian orange
Chalcedony white
Chrysoprase green
Citrine gold
Jasper black
Moonstone silver Blue
Onyx black
Quartz silver
Sardonyx red
Star rose quartz red silver
Zircon blue green

100 Pearl silver gold red
500 Black pearl black
"""

def main(args):
    print(args)
    #print(dlib.scramble(args))
    print('\n'.join(dlib.scramble(args)))

if __name__ == '__main__':
    main(sys.argv[1:])
