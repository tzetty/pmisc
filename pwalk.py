import sys
import os

DIRNAME_ONLY = 'DIRNAME_ONLY'
DEFAULT_ROOTS_FILLENAME = 'roots.txt'

def local_read_file(filename):
    ff = open(filename, 'r')
    txt = ff.read()
    ff.close()
    return txt

def local_read_file_as_dict(filename):
    result = {}
    stripped = [x.strip() for x in local_read_file(filename).split('\n')]
    lines = [x for x in stripped if len(x) > 0 and x[0] != '#']
    for line in lines:
        assert '=' in line
        parts = [x.strip() for x in line.split('=')]
        assert len(parts) == 2
        result[parts[0]] = parts[1]

    return result

def get_root_value(arg):
    roots_filename = DEFAULT_ROOTS_FILLENAME

    if arg == '@':
        return local_read_file(roots_filename).strip()

    if arg[0] == '@':
        rkey = arg[1:]
        if '::' in rkey:
            parts = rkey.split('::')
            assert len(parts) == 2
            roots_filename = parts[0]
            rkey = parts[1]

        rdict = local_read_file_as_dict(roots_filename)
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
