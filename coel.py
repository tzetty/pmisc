import sys
import random
import dlib


RAYS = [
'1st (Gwron/Virtue) Ray of Knowledge',
'2nd (Alawn/Light) Ray of Power',
'3rd (Plenydd/Harmony) Ray of Peace',
]

def print_three_rays(args):
    assert len(args) == 3

    print('Question: What do I most need to understand about this day\'s events?')
    print('')
    print('Method Used: The Three Rays of Light')
    print('')

    #print(dlib.COEL)

    #print(args)
    values = [dlib.COEL[k] for k in args]
    #print(values)
    parts = zip(args,values,RAYS)
    #print(parts)

    for part in parts:
        aa = part[0]
        bb = part[1]
        cc = part[2]
        #print('%s %s %s' % (aa,bb,cc))
        ss = '%s: "%s" %s' % (cc, aa, bb)
        print(ss)
        print('')

    print('Interpretation:')

def main(args):
    if args[0] == 'random':
        tiles = dlib.scramble(list(dlib.COEL.keys()))[0:3]
        #print(tiles)
        print_three_rays(tiles)
    else:
        print_three_rays(args)

if __name__ == '__main__':
    main(sys.argv[1:])
