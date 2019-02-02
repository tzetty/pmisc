import sys
import random
import os
import dlib

DIRNAME_ONLY = 'DIRNAME_ONLY'

def get_root_value(arg):
    if arg == '@':
        return dlib.read_file('roots.txt').strip()

    if arg[0] == '@':
        rdict = dlib.read_file_as_dict('roots.txt')
        rkey = arg[1:]
        assert rkey in rdict
        return rdict[rkey]

    return arg

def is_match(filename, exts):
    for ext in exts:
        if filename.endswith(ext):
            return True
    return False

def main(args):
    if len(args) == 0:
        print('usage: pwalk <root> [extension]+')
        print('    pwalk @shake nrkt DIRNAME_ONLY')
        return 1

    root = get_root_value(args[0])

    exts = args[1:]
    assert len(exts) > 0

    dirname_only = DIRNAME_ONLY in exts

    for dirName, subdirList, fileList in os.walk(root):
        print_dir = False
        for filename in fileList:
            if is_match(filename, exts):
                if dirname_only:
                    print_dir = True
                else:
                    fullname = os.path.join(dirName + '/' + filename)
                    print('%s' % fullname)

        if print_dir:
            print('%s' % dirName)

    return 0

if __name__ == '__main__':
    main(sys.argv[1:])
