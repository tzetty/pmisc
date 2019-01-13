#!/usr/bin/python

import random
import sys

import fr_util

# Summer and fall are calmer, winter tends toward severe.
MonthMods = {
  1: 3, 2: 2, 3: 1, 4: 0,
  5: 0, 6: 0, 7: -1, 8: -1,
  9: 0, 10: 0, 11: 1, 12: 2
}

class DayResult:
    def __init__(self, tag, adj_next):
        self.tag = tag
        self.adj_next = adj_next

    def __str__(self):
        return self.tag


class DayTableEntry:
    def __init__(self, tag, travel, adj_next, xtable=None):
        self.tag = tag
        self.travel = travel
        self.adj_next = adj_next
        self.xtable = xtable

    def describe(self):
        if self.xtable != None:
            xkeys = self.xtable.keys()
            roll = random.randint(min(xkeys), max(xkeys))
            return self.xtable[roll].describe()
        return DayResult('%s Travel: %d%%' % (self.tag, self.travel), self.adj_next)

ExpandedDayTable = {
    # description, travel percentage, adjustment for tomorrow
    1: DayTableEntry('Severe-Immediate', 100, 1),
    2: DayTableEntry('Severe-Brief', 100, 2),
    3: DayTableEntry('Severe-Sporadic', 75, 3),
    4: DayTableEntry('Severe-Frequent', 50, 4),
    5: DayTableEntry('Severe-Extended', 0, 5),
}

DayTable = {
    # description, travel percentage, adjustment for tomorrow
    1: DayTableEntry('Mild', 100, -1),
    2: DayTableEntry('Mild', 100, 0),
    3: DayTableEntry('Mild', 100, 0),
    4: DayTableEntry('Mild', 100, 0),
    5: DayTableEntry('Mild', 100, 0),
    6: DayTableEntry('Mild', 100, 0),
    7: DayTableEntry('Mild', 100, 1),
    8: DayTableEntry('Moderate', 75, 1),
    9: DayTableEntry('Difficult', 50, 2),
    10: DayTableEntry(None, None, None, ExpandedDayTable),
    11: DayTableEntry('Severe-Extended', 0, 5),
    12: DayTableEntry('Severe-Frequent', 50, 4),
    13: DayTableEntry(None, None, None, ExpandedDayTable)
}

DayTableKeyMin = min(DayTable.keys())
DayTableKeyMax = max(DayTable.keys())

def day_weather(pos, tag, day, accum):
    if tag in fr_util.Festivals:
        desc = tag
    else:
        desc = '%d %s'% (day, tag)

    month_mod = MonthMods[pos]
    raw_roll = random.randint(1,10)
    #print 'entry accum', accum, 'month_mod', month_mod, 'raw_roll', raw_roll
    roll = fr_util.limit_to_interval(raw_roll + month_mod + accum, DayTableKeyMin, DayTableKeyMax)
    weather = DayTable[roll].describe()
    print '%s: %s' % (desc, weather)

    return weather.adj_next


def main(args):
    dr = int(args[0])
    if len(args) > 1:
        accum = int(args[1])
    else:
        accum = 0

    print 'starting accum', accum
    print 'DR', dr # TODO look up roll of years name

    year = fr_util.Year(dr)
    accum = year.each_day(lambda w,x,y,z: day_weather(w,x,y,z), accum)
    print 'final accum', accum
    return 0

if __name__ == '__main__':
    main(sys.argv[1:])
