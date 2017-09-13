#namedtuple from collection class

from collections import namedtuple

color_tuple =(55,155,255)

print('color_tuple -> {}'.format(color_tuple[0]))

color_dict = {'red':55, 'blue':255, 'green':100}

print('color_dict -> {}'.format(color_dict['red']))

color_namedtuple = namedtuple('color_namedtuple', ['red', 'blue', 'green'])

color1 = color_namedtuple(55, 255, 100)
color2 = color_namedtuple(green=100, blue=90, red=70)

print('color1_namedtuple (color1[0]) -> {}'.format(color1[0]))
print('color1_namedtuple (color1.red) -> {}'.format(color1.red))

print('color2_namedtuple (color2[0]) -> {}'.format(color2[0]))
print('color2_namedtuple (color2.red) -> {}'.format(color2.red))
