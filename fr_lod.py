#!/usr/bin/python

import sys

import fr_util

class FDate:
    def __init__(self, name, day_of_year):
        self.name = name
        self.day_of_year = day_of_year

    def at_latitude_degrees(self, northern_spring_equinox_day_of_year, latitude_degrees):
        return "%s: %s" % (self.name, fr_util.mins_to_h_m(60*fr_util.hours_of_sunlight_simple(northern_spring_equinox_day_of_year, latitude_degrees, self.day_of_year)))

class FYear:
    def __init__(self, northern_spring_equinox_day_of_year, dates):
        self.northern_spring_equinox_day_of_year = northern_spring_equinox_day_of_year
        self.dates = dates

    def print_date_day_lengths(self, latitude_degrees):
        for date in self.dates:
            print date.at_latitude_degrees(self.northern_spring_equinox_day_of_year, latitude_degrees)

# FRCS p77
FrcsYear = FYear(
  80,
  [
    FDate('Hammer 15', 15),
    FDate('Midwinter', 31),
    FDate('Alturiak 15', 46),
    FDate('Ches 15', 76),
    FDate('Ches 19 Equinox', 80),
    FDate('Tarsakh 15', 106),
    FDate('Greengrass', 122),
    FDate('Mirtul 15', 137),
    FDate('Kythorn 15', 167),
    FDate('Kythorn 20 Solstice', 172),
    FDate('Flamerule 15', 197),
    FDate('Midsummer/Shieldmeet', 213),
    FDate('Eleasis 15', 228),
    FDate('Eleint 15', 258),
    FDate('Eleint 21 Equinox', 263),
    FDate('High Harvestide', 274),
    FDate('Marpenoth 15', 289),
    FDate('Uktar 15', 319),
    FDate('The Feast of the Moon', 335),
    FDate('Nightal 15', 350),
    FDate('Nightal 20 Solstice', 355)
  ]
)

# SCAG p15
ScagYear = FYear(
  122,
  [
    FDate('Hammer 15', 15),
    FDate('Midwinter Solstice', 31),
    FDate('Alturiak 15', 46),
    FDate('Ches 15', 76),
    FDate('Tarsakh 15', 106),
    FDate('Greengrass Equinox', 122),
    FDate('Mirtul 15', 137),
    FDate('Kythorn 15', 167),
    FDate('Flamerule 15', 197),
    FDate('Midsummer/Shieldmeet Solstice', 213),
    FDate('Eleasis 15', 228),
    FDate('Eleint 15', 258),
    FDate('High Harvestide', 274),
    FDate('Marpenoth 15', 289),
    FDate('Marpenoth 30 Equinox', 304),
    FDate('Uktar 15', 319),
    FDate('The Feast of the Moon', 335),
    FDate('Nightal 15', 350)
  ]
)



def main(args):
    for latitude_degrees in [float(arg) for arg in args]:
        print 'FRCS (pre 1488 DR) Latitude:', latitude_degrees
        FrcsYear.print_date_day_lengths(latitude_degrees)
        print
        print 'SCAG (post 1488 DR) Latitude:', latitude_degrees
        ScagYear.print_date_day_lengths(latitude_degrees)
        print
    return 0

if __name__ == '__main__':
    main(sys.argv[1:])
