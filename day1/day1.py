# read input
with open('input.txt', 'r') as f:
    numbers = f.readlines()

numbers = list(map(int, numbers))

# problem requires us to find two numbers that produce 2020
for i in range(0, len(numbers)-1):
    for j in range(i+1, len(numbers)):
        left = numbers[i]
        right = numbers[j]
        if left > 2020 or right > 2020:
            continue
        if left + right == 2020:
            print('Solution found at indices {} and {}'.format(i,j))
            print('{} * {} = {}'.format(left, right, left * right))

for i in range(0, len(numbers)-2):
    for j in range(i+1, len(numbers)-1):
        for k in range(j+1, len(numbers)):
            left = numbers[i]
            middle = numbers[j]
            right = numbers[k]
            if left > 2020 or middle > 2020 or right > 2020:
                continue
            if left + middle + right == 2020:
                print('Solution found at indices {}, {}, and {}'.format(i,j,k))
                print('{} * {} * {}  = {}'.format(left, middle, right, left * middle * right))