import sys
import random
import math

COEL = {
    'A': 'proceeding forward, continuation',
    'E': 'motion checked, interrupted',
    'I': 'movement of a thing to its proper place',
    'O': 'movement outward or away from',
    'W': 'sorting, classifying, categorizing',
    'Y': 'balance suspension, neutrality, pause',
    'U': 'wholeness, competeness',
    'Bi': 'quiescent state of being, mere existance',
    'Ci': 'holding, containing, comprehending',
    'Di': 'expanding unfolding, laying open',
    'Ffi': 'causation, impulsion',
    'Gi': 'attachment, cohesion appetite, desire',
    'Hi': 'generation, abudance, nurturing, support',
    'Li': 'flow, softness, smoothness',
    'Mi': 'comprehending, embracing or surrounding',
    'Ni': 'distinguishing or identifying an individual',
    'Pi': 'pushing, penetrating',
    'Ri': 'force, prevalence or superiority',
    'Si': 'inferiority, secrecy',
    'Ti': 'tension drawing or straining',
    'Ddi': 'realm, extent, field of action',
    'Lli': 'turbulence, confusion, disruption',
    'Fi': 'protection, limitation, discipline',
    'Chi': 'conflict, difficulty, opposition',
}

def scramble(seq):
    dup = [x for x in seq]
    result = []

    while len(dup) > 0:
        ndx = random.randint(0, len(dup)-1)
        result.append(dup[ndx])
        del dup[ndx]

    return result

def read_file(filename):
    ff = open(filename, 'r')
    txt = ff.read()
    ff.close()
    return txt

def read_file_as_dict(filename):
    result = {}
    stripped = [x.strip() for x in read_file(filename).split('\n')]
    lines = [x for x in stripped if len(x) > 0 and x[0] != '#']
    for line in lines:
        assert '=' in line
        parts = [x.strip() for x in line.split('=')]
        assert len(parts) == 2
        result[parts[0]] = parts[1]

    return result

def parse_csv_line(txt):
    return [x.strip() for x in txt.split(',')]

def read_csv(filename):
    txt = read_file(filename)
    return [parse_csv_line(x) for x in txt.split('\n') if len(x) > 0]

def get_column_values(lines, column_number):
    ss = set()

    for line in lines:
        ss.add(line[column_number])

    result = [x for x in ss]
    result.sort()
    return result

def get_column_match_count(lines, column_number, column_value):
    total = 0

    for line in lines:
        if line[column_number] == column_value:
            total += 1

    return total

def get_column_content(lines, prime_index, prime_value, lookup_index):
    result = {}

    for line in lines:
        value = line[prime_index]
        if value == prime_value:
            matchme = line[lookup_index]
            if matchme in result:
                result[matchme] += 1
            else:
                result[matchme] = 1

    return result

def get_global_content(lines):
    result = {}

    for line in lines:
        for value in line:
            if value in result:
                result[value] += 1
            else:
                result[value] = 1

    return result
