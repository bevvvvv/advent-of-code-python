import argparse

# get input file
parser = argparse.ArgumentParser(description='Day 1 of advent of code.')
parser.add_argument('INPUT', type=str, help='Path to input text file.')

args = parser.parse_args()

# read input
with open(args.INPUT, 'r') as f:
    sonar = [int(x) for x in f.readlines()]

increase_count = 0
for i in range(len(sonar)-1):
        if sonar[i] < sonar[i+1]:
            increase_count += 1

print('There are {} instances of increasing depth'.format(increase_count))