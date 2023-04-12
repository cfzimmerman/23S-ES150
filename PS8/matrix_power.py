from numpy import linalg
from typing import NewType

InputMatrix = NewType("IntMatrix", list[list[float]])


transition_matrix: InputMatrix = \
    [
        [0.4, 0.6, 0],
        [0.4, 0.3, 0.3],
        [0.7, 0, 0.3]
    ]


def print_matrix_pow(mx: InputMatrix, pow: int) -> None:
    ''' Prints a matrix raised to a power '''
    print(f"\nP^{pow}")
    print(linalg.matrix_power(mx, pow))


def run():
    print(f"\nFor P = {transition_matrix}")

    powers = [2, 4, 8, 16, 32, 64]

    for pw in powers:
        print_matrix_pow(transition_matrix, pw)


# run()

'''

OUTPUT:

For P = [[0.4, 0.6, 0], [0.4, 0.3, 0.3], [0.7, 0, 0.3]]

P^2
[[0.4  0.42 0.18]
 [0.49 0.33 0.18]
 [0.49 0.42 0.09]]

P^4
[[0.454  0.3822 0.1638]
 [0.4459 0.3903 0.1638]
 [0.4459 0.3822 0.1719]]

P^8
[[0.4495774  0.38529582 0.16512678]
 [0.44951179 0.38536143 0.16512678]
 [0.44951179 0.38529582 0.16519239]]

P^16
[[0.44954129 0.3853211  0.16513761]
 [0.44954128 0.3853211  0.16513761]
 [0.44954128 0.3853211  0.16513762]]

P^32
[[0.44954128 0.3853211  0.16513761]
 [0.44954128 0.3853211  0.16513761]
 [0.44954128 0.3853211  0.16513761]]

P^64
[[0.44954128 0.3853211  0.16513761]
 [0.44954128 0.3853211  0.16513761]
 [0.44954128 0.3853211  0.16513761]]

'''
