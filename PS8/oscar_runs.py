from matrix_power import InputMatrix, print_matrix_pow
from markov import walk_graph, GraphWalkStats, get_possible_states

'''

Exercise 5. 
Oscar goes for a run each morning. When he leaves his house for his run, he is equally likely
to go out either the front or back door; and similarly, when he returns, he is equally likely
to go to either the front or back door. Oscar owns only five pairs of running shoes which
he takes off immediately after the run at whichever door he happens to be. If there are no
shoes at the door from which he leaves to go running, he runs barefooted. We are interested
in determining the long-term proportion of time that he runs barefooted.
(a) Set the scenario up as a Markov chain, specifying the states and the transition prob-
abilities. Draw a diagram if it is clearer, but make sure it is clearly labeled.
(b) Determine the long-run proportion of time that Oscar runs barefoot. Please do this af-
ter Tuesday if you want to do it analytically. Alternatively, you can write a simulation
to estimate this probability

'''

transition_matrix: InputMatrix = [
    [0.75, 0.25, 0, 0, 0, 0],
    [0.25, 0.5, 0.25, 0, 0, 0],
    [0, 0.25, 0.5, 0.25, 0, 0],
    [0, 0, 0.25, 0.5, 0.25, 0],
    [0, 0, 0, 0.25, 0.5, 0.25],
    [0, 0, 0, 0, 0.25, 0.75]
]


'''

print_matrix_pow(mx=transition_matrix, pow=512)

result:
P^512
[[0.16666667 0.16666667 0.16666667 0.16666667 0.16666667 0.16666667]
 [0.16666667 0.16666667 0.16666667 0.16666667 0.16666667 0.16666667]
 [0.16666667 0.16666667 0.16666667 0.16666667 0.16666667 0.16666667]
 [0.16666667 0.16666667 0.16666667 0.16666667 0.16666667 0.16666667]
 [0.16666667 0.16666667 0.16666667 0.16666667 0.16666667 0.16666667]
 [0.16666667 0.16666667 0.16666667 0.16666667 0.16666667 0.16666667]]

'''


def run():
    # This was just for verifying the correctness of the approach above.
    NUM_STEPS = 1000000
    possible_states = get_possible_states(base=transition_matrix)
    results: GraphWalkStats = walk_graph(
        start_state=0,
        max_steps=NUM_STEPS,
        target_state=0,
        target_edge=(1, 2),
        transition_matrix=transition_matrix,
        possible_states=possible_states
    )
    print("frequency of 0: ", results["target_state_visits"] / NUM_STEPS)


'''

run()

result:
frequency of 0:  0.1662

'''
