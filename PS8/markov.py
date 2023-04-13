from matrix_power import transition_matrix, InputMatrix
from typing import TypedDict, NewType
import numpy

initial_state: InputMatrix = transition_matrix

TransitionList = NewType("TransitionList", list[InputMatrix])

MoveState = NewType("MoveState", int)
# MoveState is row index


class GraphWalkStats(TypedDict):
    target_state_visits: int
    target_edge_visits: int
    history: list[int]


def choose_next(options: list[MoveState], probabilities: list[float]) -> MoveState:
    # Given a list of moves and their probabilities, chooses a move
    assert (len(options) == len(probabilities))
    return numpy.random.choice(len(options), p=probabilities)


def get_possible_states(base: InputMatrix) -> list[MoveState]:
    # Possible states are the index number of each row in a graph.
    return list(range(len(base)))


def walk_graph(
    start_state: MoveState,
    max_steps: int,
    target_state: int,
    target_edge: tuple[int, int],
    transition_matrix: InputMatrix,
    possible_states: list[MoveState]
) -> GraphWalkStats:

    history: list[int] = []
    current_state: MoveState = start_state
    target_state_count: int = 0
    target_edge_count: int = 0

    for num in range(max_steps):

        history.append(current_state)

        next_move: MoveState = choose_next(
            options=possible_states, probabilities=transition_matrix[current_state])

        if next_move == target_state:
            target_state_count += 1

        if (current_state == target_edge[0] and next_move == target_edge[1]):
            target_edge_count += 1

        current_state = next_move

    return GraphWalkStats(
        target_state_visits=target_state_count,
        target_edge_visits=target_edge_count,
        history=history
    )


def run():
    NUM_STEPS: int = 100000
    possible_states = get_possible_states(base=initial_state)
    results: GraphWalkStats = walk_graph(
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
