import argparse

import numpy as np

# get input file
parser = argparse.ArgumentParser(description='Day 3 of advent of code')
parser.add_argument('INPUT', type=str, help='Path to input text file.')

args = parser.parse_args()

# read input
with open(args.INPUT, 'r') as f:
    binary_numbers = [bi_num for bi_num in f.readlines()]

num_count = len(binary_numbers)
gamma_counts = [0]

binary_matrix = []
for num in binary_numbers:
    binary_matrix.append([int(digit) for digit in num if digit != '\n'])

binary_matrix = np.array(binary_matrix)
row_totals = np.sum(binary_matrix, axis=0)
gamma_vals = [int(boolean) for boolean in row_totals > (num_count - row_totals)]
epsilon_vals = -1 * (np.array(gamma_vals) - 1)

gamma_rate = int(''.join(map(str, gamma_vals)), 2)
eps_rate = int(''.join(map(str, epsilon_vals)), 2)

print('The gamma rate is {} and the epsilon rate is {}'.format(gamma_rate, eps_rate))
print('Power consumption is {}'.format(gamma_rate*eps_rate))

# oxygen search
def rating_search(binary_matrix, col_num, most=True):
    num_count = binary_matrix.shape[0]
    if num_count == 1:
        return list(binary_matrix[0,:])
    else:
        search_col = binary_matrix[:,col_num]
        total_1 = np.sum(search_col)
        
        one_most = total_1 > (num_count - total_1)
        even = total_1 == (num_count - total_1)
        bit_criteria = 0
        if most and one_most:
            bit_criteria = 1
        elif most and even:
            bit_criteria = 1
        elif not most and not one_most and not even:
            bit_criteria = 1

        filter_results = binary_matrix[np.argwhere(search_col == bit_criteria)[:,0],:]

        return rating_search(filter_results, col_num+1, most)

oxygen_gen_rating = rating_search(np.array(binary_matrix), 0)
co2_scrubber_rating = rating_search(np.array(binary_matrix), 0, False)

oxygen_gen_rating = int(''.join(map(str, oxygen_gen_rating)), 2)
co2_scrubber_rating = int(''.join(map(str, co2_scrubber_rating)), 2)

print('The oxygen generator rating is {}'.format(oxygen_gen_rating))
print('The CO2 scrubber rating is {}'.format(co2_scrubber_rating))
print('The life support rating is {}'.format(oxygen_gen_rating * co2_scrubber_rating))