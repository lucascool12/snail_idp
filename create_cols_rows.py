import sys
import math
from typing import Tuple
from functools import lru_cache


# https://math.stackexchange.com/questions/3157030/parametrizing-the-square-spiral
@lru_cache(maxsize=None)
def square_spiral(n) -> Tuple[int, int]:
    n_sqrt = math.sqrt(n)
    n_floor = math.floor(n_sqrt)
    n_capped = n_floor if n_floor%2 == 0 else n_floor -1
    n_capped2 = n_capped*n_capped
    if n_capped2 <= n <= (n_capped2 + n_capped):
        return (math.ceil(-n_capped/2 + n - n_capped2), math.ceil(n_capped/2))
    elif (n_capped2 + n_capped) < n <= (n_capped2 + 2*n_capped + 1):
        return (math.ceil(n_capped/2), math.ceil(n_capped/2 - n + n_capped2 + n_capped))
    elif (n_capped2 + 2*n_capped + 1) < n <= (n_capped2 + 3*n_capped + 2):
        return (math.ceil(n_capped/2 - n + n_capped2 + 2*n_capped + 1), math.ceil(-n_capped/2 - 1))
    # elif (n_capped2 + 3*n_capped + 2) < n <= (n_capped2 + 4*n_capped + 3):
    else:
        return (int(-n_capped/2 - 1), int(-n_capped/2 -1 + n - n_capped2 - 3*n_capped - 2))

def transform_points(x, y, size) -> Tuple[int, int]:
    return (-x + size//2, y + math.floor(size/2))

if __name__ == "__main__":
    numb = int(sys.argv[1])
    if numb%2 != 1:
        print("Needs to be uneven number")
        exit(0)
    print(f"LastCell := {numb*numb}.")
    values = "Cell := { "
    for i in range(1, numb*numb):
        values += f"{i}, "
    values += f"{numb*numb} }}.\n\n"
    print(values)
    a = math.floor(math.log10(numb*numb))
    def sort_key(x):
        return int(x[1]*10**(1+a) + x[0])
    vals_row =\
        [(i, transform_points(*square_spiral(numb*numb - i - 1), numb)[0])\
         for i in range(0, numb*numb)]
    vals_row.sort(key=sort_key)
    vals_cols =\
        [(i, transform_points(*square_spiral(numb*numb - i - 1), numb)[1])\
         for i in range(0, numb*numb)]
    vals_cols.sort(key=sort_key)
    cols = "Column := { "
    for j, (i, y) in enumerate(vals_cols):
        if j != len(vals_cols) - 1:
            cols += f"{i + 1} -> {y%numb + 1}, "
        else:
            cols += f"{i + 1} -> {y%numb + 1}\n}}.\n"
            break
        if j%numb + 1 == numb:
            cols += "\n\t"
    print(cols)
    cols = "Row := { "
    for j, (i, x) in enumerate(vals_row):
        if j != len(vals_row) - 1:
            cols += f"{i + 1} -> {x%numb + 1}, "
        else:
            cols += f"{i + 1} -> {x%numb + 1}\n}}.\n"
            break
        if j%numb + 1 == numb:
            cols += "\n\t"
    print(cols)


