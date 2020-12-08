# read input
with open('input.txt', 'r') as f:
    lines = f.readlines()

valid = 0
valid_two = 0
for idx, line in enumerate(lines):
    pair = line.split(':')
    policy = pair[0].strip()
    password = pair[1].strip()

    policy = policy.split(' ')
    policy_letter = policy[1]
    policy_limits = policy[0].split('-')
    policy_min = int(policy_limits[0])
    policy_max = int(policy_limits[1])

    occurences = password.count(policy_letter)

    if occurences <= policy_max and occurences >= policy_min:
        valid += 1

    # found in exactly one of the two spaces
    if password[policy_min-1] == policy_letter and password[policy_max-1] != policy_letter:
        valid_two += 1
    if password[policy_min-1] != policy_letter and password[policy_max-1] == policy_letter:
        valid_two += 1

print('There are {} valid passwords from policy format one'.format(valid))
print('There are {} valid passwords from policy format two'.format(valid_two))
