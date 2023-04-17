import sys  # noqa
sys.path.append("..")  # noqa
from PS8 import Markov, InputMatrix, GraphWalkStats

seasons: InputMatrix = [
    # [Fall, Golden, Winter, Spring, Summer, Bitter]
    # Fall
    [(2/3), (1/6), (1/6), 0, 0, 0],
    # Golden
    [0, 1, 0, 0, 0, 0],
    # Winter
    [(1/5), (1/10), (1/2), (1/5), 0, 0],
    # Spring
    [0, 0, 0, 0, 1, 0],
    # Summer
    [0, 0, 0, (1/2), (1/4), (1/4)],
    # Bitter
    [0, 0, 0, 0, (1/4), (3/4)],
]


def run():
    # This was just for verifying the correctness of the approach above.
    NUM_STEPS = 10000000
    possible_states = Markov.get_possible_states(base=seasons)
    if not Markov.valid_transition_matrix(seasons):
        raise ValueError
    target_state = 5
    results: GraphWalkStats = Markov.walk_graph(
        start_state=3,
        max_steps=NUM_STEPS,
        target_state=target_state,
        target_edge=(1, 2),
        transition_matrix=seasons,
        possible_states=possible_states
    )
    print(f"frequency of {target_state}: ",
          results["target_state_visits"] / NUM_STEPS)


# run()

'''

For t_0 = Spring, NUM_STEPS = 10,000,000
pi = [Fall, Golden, Winter, Spring, Summer, Bitter]

pi_n = [0.0, 0.0, 0.0, 0.1999237, 0.3997449, 0.3999143]

Rounding approximations:
pi_n = [0.0, 0.0, 0.0, 0.2, 0.4, 0.4]

'''
