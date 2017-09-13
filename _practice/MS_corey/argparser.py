#argparser.py
#This program calculates the volume of a cylinder given RADIUS and HEIGHT
# Cylinder Volume = (pi) * (radius ** 2) * (height)

import math
import argparse

parser = argparse.ArgumentParser(description='Calculate volume of Cylinder')
parser.add_argument('-r','--radius', type=int, required=True, metavar='', help='Radius of Cylinder')
parser.add_argument('-H', '--height', type=int, required=True, metavar='', help='Height of Cylinder')
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='print quiet')
group.add_argument('-v', '--verbose', action='store_true', help='print verbose')
args = parser.parse_args()


def cylinder_volume(radius, height):
	vol = (math.pi) * (radius **2 ) * (height)
	return vol

if __name__ == '__main__':
	volume = cylinder_volume(args.radius, args.height)
	if args.quiet:
		print volume
	elif args.verbose:
		print('Volume of a Cylinder with radius {} and Height {} is :- {}'.format(args.radius, args.height, volume))
	else:
		print('Voluem of Cylinder is :- {}'.format(volume))