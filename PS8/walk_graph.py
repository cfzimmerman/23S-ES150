from Markov import Markov, InputMatrix, GraphWalkStats
from matrix_power import transition_matrix

initial_state: InputMatrix = transition_matrix


def run():
    NUM_STEPS: int = 100000
    possible_states = Markov.get_possible_states(base=initial_state)
    results: GraphWalkStats = Markov.walk_graph(
        start_state=0,
        max_steps=NUM_STEPS,
        target_state=1,
        target_edge=(1, 2),
        transition_matrix=initial_state,
        possible_states=possible_states
    )
    print("# State 1 Visits: ", results["target_state_visits"])
    print("# Edge 1-2 Visits: ", results["target_edge_visits"])


# run()

'''

Output for n = 100,000 

# State 1 Visits:  38497
# Edge 1-2 Visits:  11608

pi_100000 = 38,437 / 100,000 = 0.38497
edge_100000 = 11,608 / 100,000 = 0.11608

'''
