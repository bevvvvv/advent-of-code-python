import argparse
from os import curdir

# get input file
parser = argparse.ArgumentParser(description='Day 1 of advent of code.')
parser.add_argument('INPUT', type=str, help='Path to input text file.')
parser.add_argument('--window', action="store_true", default=False, help='Whether to calculate using 3 measurement window')

args = parser.parse_args()

# read input
with open(args.INPUT, 'r') as f:
    sonar = [int(x) for x in f.readlines()]

increase_count = 0
window = 3 if args.window else 1
for i in range(len(sonar)-window):
        curr = sonar[i:i+window]
        next = sonar[i+1:i+1+window]
        
        if sum(curr) < sum(next):
            increase_count += 1

print('There are {} instances of increasing depth'.format(increase_count))