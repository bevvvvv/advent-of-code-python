import argparse

import numpy as np

# get input file
parser = argparse.ArgumentParser(description='Day 2 of advent of code')
parser.add_argument('INPUT', type=str, help='Path to input text file.')
parser.add_argument('--aim', action="store_true", default=False, help='Whether to calculate using aim')

args = parser.parse_args()

# read input
with open(args.INPUT, 'r') as f:
    instructions = [tuple(line.split(' ')) for line in f.readlines()]

h_pos = 0
depth = 0
aim = 0
for instruction in instructions:
    direction = instruction[0]
    dist = int(instruction[1])
    if direction == 'forward':
        h_pos += dist
        depth += aim * dist
    elif direction == 'down':
        aim += dist
    else:
        aim -= dist

if not args.aim:
    depth = aim

print('The horizontal position is {} and depth is {}'.format(h_pos, depth))
print('Multiply to get {}'.format(h_pos*depth))