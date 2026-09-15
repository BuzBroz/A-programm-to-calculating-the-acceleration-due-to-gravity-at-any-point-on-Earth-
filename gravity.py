# Copyright (c) 2025 Alexander Buzoverya, Konstantin Buzoverya
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

#!/bin/python3

import numpy as np
import argparse

parser = argparse.ArgumentParser(
  description='calculate surface acceleration of gravity for a given latitude')
parser.add_argument('--lat', type=float, default = 56.297336,
  help = 'latitude in decimal degrees (56.297336 by default)')
parser.add_argument('--elev', type=float, default = 190,
  help = 'elevation abov sea level in meters (190 by default)')
args = parser.parse_args()
h = args.elev
lat_d = args.lat # Latitude, an angle in decimal degrees

pi = np.pi
lat = (lat_d * pi) / 180 # Latitude, an angle in radians
print()
print(f"Latitude (decimal degrees): {lat_d:}")
print(f"Ellipsoidal elevation (m): {h:}")

sin1 = np.sin(lat)
sin2 = np.sin(lat * 2)
cos1 = np.cos(lat)

# World Geodetic System 84 (WGS84)
g = 9.7803253359 # Surface gravity at the equator (WGS84)
c1 = 0.001931852652
c2 = 0.0066943799901

# Gravity on the ellipsoidal surface (normal gravity)
g0 = g * (1 + c1 * sin1**2) / (np.sqrt(1 - c2 * sin1**2))

print()
print("World Geodetic System 84 (WGS84)")
print(f"\tAcceleration of gravity at sea level (m/s^2): {g0:.9}")	

f = 1/298.257223563
w = 7292115.0e-11 # rad/s
gm = 3986004.418e8 # m3/s2
a = 6378137.0 # m
b = 6356752.3142 # m
m = w**2 * a**2 * b / gm # m = 0.00344978650684

# Gravity at the ellipsoidal elevation
gh = g0 * (1 - 2 * h * (1 + f + m - 2 * f * sin1**2) / a + 3 * h**2/a**2)
print(f"\tAcceleration of gravity at elevation (m/s^2): {gh:.9}")
#
# Параметры Земли 1990 года (ПЗ-90.11)
#
print()
print("Параметры Земли 1990 года (ПЗ-90.11)")
с1 = 0.0053024
с2 = 0.0000058
ge = 978032.84 # Surface gravity at the equator)
g0 = ge * (1 + с1 * sin1**2 - с2 * sin2**2)
gh = g0 - 0.3086 * h
g0 = g0 * 1e-5
gh = gh * 1e-5

# Ускорения нормальной силы тяжести на поверхности общеземного эллипсоида (ОЗЭ)
print(f"\tAcceleration of gravity at sea level (m/s^2): {g0:.9}")
# Ускорения нормальной силы тяжести на высоте над ОЗЭ
print(f"\tAcceleration of gravity at elevation (m/s^2): {gh:.9}")