#!/usr/bin/python

import math
import sys

def limit_to_interval(x, min_value, max_value):
    return max(min(x, max_value), min_value)

def d2r(d):
  return d*math.pi/180.0

def r2d(r):
  return r*180.0/math.pi

# from Candlekeep discussion with Ed Greenwood 31 December 2004
# http://www.forum.candlekeep.com/topic.asp?TOPIC_ID=1901&whichpage=80&SearchTerms=axial%2Ctilt
AXIAL_TILT_DEGREES = 28.883333
SOLAR_DAYS_PER_YEAR = 365.0

HOURS_PER_SOLAR_DAY = 24.0
DEGREES_PER_HOUR = 360.0 / HOURS_PER_SOLAR_DAY

# calculations based on:
# http://www.jgiesen.de/astro/solarday.htm
# (site contains errors, which have been corrected here)

def delta_from_day_of_year_simple(northern_spring_equinox_day_of_year, day_of_year):
  orbital_position_degrees = (day_of_year-northern_spring_equinox_day_of_year)/SOLAR_DAYS_PER_YEAR
  return -1 * AXIAL_TILT_DEGREES * math.sin(2*math.pi*orbital_position_degrees)

def hours_of_sunlight_simple(northern_spring_equinox_day_of_year, latitude_degrees, day_of_year):
  delta = delta_from_day_of_year_simple(northern_spring_equinox_day_of_year, day_of_year)
  return r2d(math.acos(math.tan(d2r(latitude_degrees))*math.tan(d2r(delta)))) / (DEGREES_PER_HOUR / 2.0)

def mins_to_h_m(mins):
    return '%dh %dm' % (int(mins/60), int(mins - int(mins/60)*60))


class Month:
    def __init__(self, pos, tag, length, leap_only = False):
        self.pos = pos
        self.tag = tag
        self.length = length
        self.leap_only = leap_only

    def apply(self, fn, accum=None):
        for day in range(self.length):
            accum = fn(self.pos, self.tag, day+1, accum)
        return accum

Festivals = [
    'Midwinter',
    'Greengrass',
    'Midsummer',
    'Shieldmeet',
    'High Harvestide',
    'Feast of the Moon'
]

class Year:
    months = [
        Month(1, 'Hammer', 30),
        Month(1, 'Midwinter', 1),
        Month(2, 'Alturiak', 30),
        Month(3, 'Ches', 30),
        Month(4, 'Torsak', 30),
        Month(4, 'Greengrass', 1),
        Month(5, 'Mirtul', 30),
        Month(6, 'Kythorn', 30),
        Month(7, 'Flamerule', 30),
        Month(7, 'Midsummer', 1),
        Month(7, 'Shieldmeet', 1, True),
        Month(8, 'Eleasis', 30),
        Month(9, 'Eleint', 30),
        Month(9, 'High Harvestide', 1),
        Month(10, 'Marpenoth', 30),
        Month(11, 'Uktar', 30),
        Month(11, 'Feast of the Moon', 1),
        Month(12, 'Nightal', 30)
    ]

    def __init__(self, dr):
        self.dr = dr
        if (dr % 4) == 0:
            self.is_leap = True
        else:
            self.is_leap = False

    def each_day(self, fn, accum=0):
        for month in self.months:
            if (month.leap_only == True) and (self.is_leap == False):
                pass
            else:
                accum = month.apply(fn, accum)
        return accum

if __name__ == '__main__':
    print 'fr_util is not an executable module'
