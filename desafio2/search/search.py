# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from random import shuffle
from util import Stack, Queue, PriorityQueue


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    """
    actions = Stack()  # stack structure (from utils)
    visited_states = []  # visited states

    # if initial state is the goal state (stop)
    if problem.isGoalState(problem.getStartState()):
        return []

    # Push initial state and path to it (empty path)
    actions.push((problem.getStartState(), []))

    # Stop when solution is found
    while not actions.isEmpty():
        # get current state and path to it
        current_state, path_to_state = actions.pop()

        # verify if state is goal state
        if problem.isGoalState(current_state):
            return path_to_state

        if current_state not in visited_states:
            # add state in list of visited states
            visited_states.append(current_state)

            # Get child nodes of current state
            child_states = problem.getSuccessors(current_state)
            # shuffle(child_states)

            if len(child_states) > 0:
                # add child nodes to list of actions
                for node in child_states:
                    state, direction, cost = node
                    if state not in visited_states:
                        child_path = path_to_state + [direction]
                        actions.push((state, child_path))

    return []


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    actions = Queue()  # stack structure (from utils)
    visited_states = []  # visited states

    # if initial state is the goal state (stop)
    if problem.isGoalState(problem.getStartState()):
        return []

    # Push initial state and path to it (empty path)
    initial_node = (problem.getStartState(), [])
    actions.push(initial_node)

    # Stop when solution is not found
    while not actions.isEmpty():
        # get current state and path to it
        current_state, path_to_state = actions.pop()
        # print(path_to_state)

        # verify if state is goal state
        if problem.isGoalState(current_state):
            return path_to_state

        if current_state not in visited_states:
            # add state in list of visited states
            visited_states.append(current_state)

            # Get child nodes of current state
            child_states = problem.getSuccessors(current_state)
            shuffle(child_states)

            if len(child_states) > 0:
                # add child nodes to list of actions
                for node in child_states:
                    state, direction, cost = node
                    if state not in visited_states:
                        child_path = path_to_state + [direction]
                        actions.push((state, child_path))

    return []
    # initial_node = (problem.getStartState(), [])
    #
    # if problem.isGoalState(initial_node.state):
    #     return initial_node.actions
    #
    # frontier = Queue()
    # frontier.push(initial_node)
    # explored = set()
    #
    # while not frontier.isEmpty():
    #     current_node = frontier.pop()
    #     explored.add(current_node.state)
    #     for state, action, cost in problem.getSuccessors(current_node.state):
    #         child_node = state, action, cost
    #         if child_node.state not in explored and child_node not in frontier.list:
    #             if problem.isGoalState(child_node.state):
    #                 return child_node.actions
    #             frontier.push(child_node)
    #
    # return []


def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    frontier = PriorityQueue()  # frontier
    visited_states = []  # list of visited states
    node = problem.getStartState()  # initial node

    # if initial state is the goal state (stop)
    if problem.isGoalState(node):
        return []

    # push initial state in PriorityQueue
    frontier.push((node, []), 0)

    # stop when solution is found or when queue is empty
    while not frontier.isEmpty():
        current_state, path_to_state = frontier.pop()  # choose the lowest cost node

        if problem.isGoalState(current_state):
            return path_to_state

        if current_state not in visited_states:
            # add current state in visited states
            visited_states.append(current_state)

            # get child nodes
            child_states = problem.getSuccessors(current_state)

            if len(child_states) > 0:
                # add child nodes to list of actions
                for node in child_states:
                    state, direction, cost = node
                    path_to_child = path_to_state + [direction]
                    path_cost = problem.getCostOfActions(path_to_child)
                    frontier_states = {state: priority for priority, _, (state, directions) in frontier.heap}

                    if state not in visited_states or state not in frontier_states:
                        frontier.push((state, path_to_child), path_cost)
                    elif state in frontier_states and frontier_states[state] > path_cost:
                        frontier.update((state, path_to_child), path_cost)
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch  # to be implemented
dfs = depthFirstSearch
astar = aStarSearch  # to be implemented
ucs = uniformCostSearch  # to be implemented
