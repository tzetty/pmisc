import sys
import random
import math
import dlib


def main(args):

    lines = None
    for opcode in args:
        if lines == None:
            lines = dlib.read_csv(opcode)
            for line in lines:
                print(line)

        elif opcode == 'clear':
            lines = None
        elif opcode == 'global':
            cc = dlib.get_global_content(lines)
            keys = list(cc.keys())
            keys.sort()
            print(', '.join(('%s:%d' % (key,cc[key]) for key in keys)))
        elif '?' in opcode:
            parts = opcode.split('?')
            prime_index =  int(parts[0])
            lookup_index =  int(parts[1])

            prime_keys = dlib.get_column_values(lines, prime_index)
            for prime_key in prime_keys:
                cc = dlib.get_column_content(lines, prime_index, prime_key, lookup_index)
                keys = list(cc.keys())
                keys.sort()
                print('%s: %s' % (prime_key, ', '.join(('%s:%d' % (key,cc[key]) for key in keys))))

        else:
            column_index = int(opcode)
            print(column_index)
            keys = dlib.get_column_values(lines, column_index)
            #print(keys)
            for key in keys:
                count = dlib.get_column_match_count(lines, column_index, key)
                print('%s: %d' % (key, count))
        print('')

if __name__ == '__main__':
    main(sys.argv[1:])
