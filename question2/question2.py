FACTORIAL_MEMO = [1, 1]

def factorial(num):
    """Return the factorial of the integer num."""
    assert isinstance(num, int)
    while num >= len(FACTORIAL_MEMO):
        FACTORIAL_MEMO.append(len(FACTORIAL_MEMO) * FACTORIAL_MEMO[-1])
    return FACTORIAL_MEMO[num]

def binomial_coeff(n_in, k_in):
    """Return the binomial coefficient (n; k), i.e. n choose k."""
    assert isinstance(n_in, int) and isinstance(k_in, int)
    return factorial(n_in) // (factorial(k_in) * factorial(n_in - k_in))

def probability(n_in, k_in, p_in):
    """
    Return the probability of getting k heads on n flips of a not-necessarily-fair coin,
    with probability p of getting heads.
    """
    assert 0. <= p_in <= 1.
    return binomial_coeff(n_in, k_in) * p_in**k_in * (1 - p_in)**(n_in - k_in)

def input_safe_int(first_prompt, try_again_prompt):
    got_raw = input(first_prompt)
    while isinstance(got_raw, str):
        try:
            got_raw = int(got_raw)
        except ValueError:
            got_raw = input(try_again_prompt)
    assert isinstance(got_raw, int)
    return got_raw

print('Part a')
n = input_safe_int('n?: ', 'try again. n?: ')
k = input_safe_int('k?: ', 'try again. k?: ')
print(n, 'choose', k, '=', binomial_coeff(n, k))

print('Part b')
# The largest coefficient will be 20 choose 10. So find its length, and fit
# each number within that size. The longest row will be at the bottom 
# (the 20th). So make sure each row has that length; centre its contents
# within that size.
num_size = len(str(binomial_coeff(20, 10)))
last_row = '  '.join(
    [
        '{num:^{size}}'.format(num=binomial_coeff(20, it), size=num_size) 
        for it in range(21)
    ]
)

for row in range(20):
    row_nums = []
    for col in range(row + 1):
        row_nums.append(binomial_coeff(row, col))
    curr_line = '  '.join(
        [
            '{num:^{size}}'.format(num=elem, size=num_size) for elem in row_nums
        ]
    )
    print('{line:^{row_size}}'.format(line=curr_line, row_size=len(last_row))) 
print(last_row)

print('Part c')
# let's do the thing with the guy and the baseball
print('A batter has batting avg. p =.250. What is prob. of hitting at least' 
    'once in four tries?')
print('Answer: equal to 1 - prob. of hitting 0 times')
print("it's", 1 - probability(4, 0, 0.25))

print('Part d')
import random
NUM_GOAL = 1
NUM_TRIES = 4
PROBABILITY = 0.25
REPLICATES = (10, 100, 1000, 100000)
for num_reps in REPLICATES:
    success_games = 0
    for game in range(num_reps):
        hits = 0
        for attempt in range(NUM_TRIES):
            if random.random() < PROBABILITY:
                hits += 1
        if hits >= NUM_GOAL:
            success_games += 1
    print('In', num_reps, 'games, the batter obtained at least one hit in',
        success_games, 'games, for a percentage of', success_games / num_reps)
