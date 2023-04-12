from matrix_power import transition_matrix, InputMatrix
from typing import TypedDict, NewType
import numpy

'''

Generate the transition matrix for every t between 0 and 100,000

Starting at t = 1, iterate to 100,000
    For every time t
    Determine where to transition to next
    Log the next transition destination
    Log the transition edge taken
    Follow the transition

Determine where to transition to next


'''

NUM_STEPS: int = 200

initial_state: InputMatrix = transition_matrix

TransitionList = NewType("TransitionList", list[InputMatrix])

MoveState = NewType("MoveState", int)
# MoveState is row index


class GraphWalkStats(TypedDict):
    target_state_visits: int
    target_edge_visits: int


def choose_next(options: list[MoveState], probabilities: list[float]) -> MoveState:
    # Given a list of moves and their probabilities, chooses a move
    assert (len(options) == len(probabilities))
    return numpy.random.choice(len(options), p=probabilities)


def get_transition_powers(start: int, stop: int, base: InputMatrix, accumulator: InputMatrix, results: TransitionList) -> TransitionList:
    # Returns an array of transition matrices where the index corresponds to the time value
    if start > stop:
        return results
    if start < 0:
        # Power should be 0 or greater
        raise ValueError
    if start == 0:
        # First case
        new_accumulator = numpy.linalg.matrix_power(base, 0)
        return get_transition_powers(start=start + 1, stop=stop, base=base, accumulator=new_accumulator, results=[new_accumulator])
    # Normal recursive case
    assert (len(results) > 0)
    new_accumulator = numpy.matmul(base, accumulator)
    new_results = results + [new_accumulator]
    return get_transition_powers(start=start + 1, stop=stop, base=base, accumulator=new_accumulator, results=new_results)


def get_possible_states(base: InputMatrix) -> list[MoveState]:
    # Possible states are the index number of each row in a graph.
    return list(range(len(base)))


def walk_graph(
    current_state: MoveState,
    current_step: int,
    max_step: int,
    target_state: int,
    st_ct: int,
    target_edge: tuple[int, int],
    ed_ct: int,
    transitions: TransitionList,
    possible_states: list[MoveState]
) -> GraphWalkStats:
    if (current_step > max_step):
        return GraphWalkStats(
            target_state_visits=st_ct,
            target_edge_visits=ed_ct
        )
    next_move: MoveState = choose_next(options=possible_states,
                                       probabilities=transitions[current_step][current_state])

    if next_move == target_state:
        st_ct += 1

    if (current_state == target_edge[0] and next_move == target_edge[1]
            or current_state == target_edge[1] and next_move == target_edge[0]):
        ed_ct += 1

    return walk_graph(
        current_state=next_move,
        current_step=current_step + 1,
        max_step=max_step,
        target_state=target_state,
        st_ct=st_ct,
        target_edge=target_edge,
        ed_ct=ed_ct,
        transitions=transitions,
        possible_states=possible_states
    )


def run():
    transitions = get_transition_powers(
        start=0, stop=NUM_STEPS, base=initial_state, accumulator=initial_state, results=[])
    possible_states = get_possible_states(base=initial_state)
    results: GraphWalkStats = walk_graph(
        current_state=0,
        current_step=0,
        max_step=NUM_STEPS,
        target_state=1,
        st_ct=0,
        target_edge=(1, 2),
        ed_ct=0,
        transitions=transitions,
        possible_states=possible_states
    )
    print("# State 1 Visits: ", results["target_state_visits"])
    print("# Edge 1-2 Visits: ", results["target_edge_visits"])


run()
