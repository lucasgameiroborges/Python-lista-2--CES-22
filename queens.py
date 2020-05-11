import random
import time

def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)        # Calc the absolute y distance
    dx = abs(x1 - x0)        # CXalc the absolute x distance
    return dx == dy          # They clash if dx == dy


def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):     # Look at all columns to the left of c
          if share_diagonal(i, bs[i], c, bs[c]):
              return True

    return False           # No clashes - col c has a safe placement.


def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1, len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False


rng = random.Random()   # Instantiate a generator

bd = list(range(18))     # Generate the initial permutation
num_found = 0
tries = 0
t0 = time.process_time()
while num_found < 10:
    rng.shuffle(bd)
    tries += 1
    if not has_clashes(bd):
        t1 = time.process_time()
        print("# Found solution {0} in {1} tries. Time elapsed: {2}".format(bd, tries, t1-t0))
        t0 = t1
        tries = 0
        num_found += 1

# ITEM 4 LISTA 2: até tamanho 18 o programa resolve em menos de 1 minuto normalmente
#
# Tamanho 16:
# Found solution [5, 11, 4, 6, 12, 3, 13, 0, 14, 8, 1, 7, 9, 2, 15, 10] in 262247 tries. Time elapsed: 4.8125
# Found solution [1, 7, 14, 8, 0, 12, 4, 11, 5, 3, 9, 13, 15, 2, 6, 10] in 1548598 tries. Time elapsed: 28.140625
# Found solution [15, 12, 10, 8, 1, 5, 2, 9, 14, 0, 4, 6, 13, 11, 7, 3] in 2605724 tries. Time elapsed: 49.8125
# Found solution [0, 3, 10, 7, 5, 12, 15, 13, 11, 6, 8, 2, 4, 1, 9, 14] in 711907 tries. Time elapsed: 13.46875
# Found solution [0, 9, 4, 15, 13, 11, 1, 8, 5, 3, 14, 10, 2, 6, 12, 7] in 105114 tries. Time elapsed: 1.921875
#
# Tamanho 12:
# Found solution [6, 3, 9, 2, 4, 8, 11, 5, 1, 10, 0, 7] in 40036 tries. Time elapsed: 0.609375
# Found solution [4, 6, 9, 3, 1, 11, 7, 2, 0, 5, 8, 10] in 25813 tries. Time elapsed: 0.375
# Found solution [5, 8, 1, 4, 10, 7, 2, 11, 3, 6, 0, 9] in 57268 tries. Time elapsed: 0.765625
# Found solution [5, 9, 11, 3, 0, 4, 10, 8, 6, 2, 7, 1] in 18595 tries. Time elapsed: 0.25
# Found solution [2, 0, 10, 7, 5, 8, 11, 1, 3, 9, 6, 4] in 22604 tries. Time elapsed: 0.3125
#
# Tamanho 4:
# Found solution [1, 3, 0, 2] in 1 tries. Time elapsed: 0.0
# Found solution [1, 3, 0, 2] in 3 tries. Time elapsed: 0.0
# Found solution [2, 0, 3, 1] in 17 tries. Time elapsed: 0.0
# Found solution [1, 3, 0, 2] in 12 tries. Time elapsed: 0.0
# Found solution [1, 3, 0, 2] in 3 tries. Time elapsed: 0.0


