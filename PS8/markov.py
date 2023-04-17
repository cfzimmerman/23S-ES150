from typing import NewType
from abc import abstractmethod
import math
from numpy import linalg, random
import math
from typing import TypedDict, NewType


InputMatrix = NewType("IntMatrix", list[list[float]])

MoveState = NewType("MoveState", int)
# MoveState is row index


class GraphWalkStats(TypedDict):
    target_state_visits: int
    target_edge_visits: int
    history: list[int]


class Markov:
    @abstractmethod
    def print_matrix_pow(mx: InputMatrix, pow: int) -> None:
        ''' Prints a matrix raised to a power '''
        print(f"\nP^{pow}")
        print(linalg.matrix_power(mx, pow))

    @abstractmethod
    def valid_transition_matrix(m: InputMatrix) -> bool:
        ''' Returns true if the given matrix is a valid transition matrix '''
        for row in m:
            if len(row) != len(m) or math.fsum(row) != 1:
                return False
        return True

    @abstractmethod
    def __choose_next(options: list[MoveState], probabilities: list[float]) -> MoveState:
        ''' Given a list of moves and their probabilities, chooses a move '''
        assert (len(options) == len(probabilities))
        return random.choice(len(options), p=probabilities)

    @abstractmethod
    def get_possible_states(base: InputMatrix) -> list[MoveState]:
        ''' Possible states are the index number of each row in a graph. '''
        return list(range(len(base)))

    @abstractmethod
    def walk_graph(
        start_state: MoveState,
        max_steps: int,
        target_state: int,
        target_edge: tuple[int, int],
        transition_matrix: InputMatrix,
        possible_states: list[MoveState]
    ) -> GraphWalkStats:
        ''' Given a markov chain and configuration info, walks the Markov chain. '''
        history: list[int] = []
        current_state: MoveState = start_state
        target_state_count: int = 0
        target_edge_count: int = 0

        for num in range(max_steps):

            history.append(current_state)

            next_move: MoveState = Markov.__choose_next(
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
