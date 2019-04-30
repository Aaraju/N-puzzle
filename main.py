from time import time
import pydotplus
from collections import deque

state = [1, 3, 4, 8, 6, 2, 7, 0, 5]


def breadth_first_search(root):
    print("Starting Node(root) : %s" % root)
    graph = pydotplus.Dot(graph_type='digraph')
    if root.is_goal():
        return root.get_solution()
    queue = deque([root])
    visited = []
    while True:
        node = queue.popleft()
        # print("\n Parent Node : %s ,Currently popped node %s " % (node.parent, node.state,))
        # print(node.action)
        if str(node) in visited:
            continue
        visited.append(str(node))
        graph.add_node(node.dot)
        if node.parent:
            graph.add_edge(pydotplus.Edge(node.parent.dot, node.dot))
        if node.is_goal():
            graph.write_png('solution.png')
            return node.get_solution()
        queue.extend(node.successor_node())


class Node:
    goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    num_of_instances = 0

    def __str__(self):
        return self.state.__str__()

    def __init__(self, state, parent, action):
        self.parent = parent
        self.state = state
        self.action = action
        Node.num_of_instances += 1
        self.dot = pydotplus.Node(str(self), shape='plaintext')

    def __str__(self):
        return str(self.state[0:3]) + '\n' + str(self.state[3:6]) + '\n' + str(self.state[6:9])

    def is_goal(self):
        return self.state == self.goal_state

    @staticmethod
    def find_legal_actions(i, j):
        legal_action = ['U', 'D', 'L', 'R']
        if i == 0:  # up is disable
            legal_action.remove('U')
        elif i == 2:  # down is disable
            legal_action.remove('D')
        if j == 0:
            legal_action.remove('L')
        elif j == 2:
            legal_action.remove('R')
        return legal_action

    def successor_node(self):
        children = []
        x = self.state.index(0)
        i = int(x / 3)
        j = int(x % 3)
        legal_actions = self.find_legal_actions(i, j)

        for action in legal_actions:
            new_state = self.state.copy()
            if action is 'U':
                new_state[x], new_state[x - 3] = new_state[x - 3], new_state[x]
            elif action is 'D':
                new_state[x], new_state[x + 3] = new_state[x + 3], new_state[x]
            elif action is 'L':
                new_state[x], new_state[x - 1] = new_state[x - 1], new_state[x]
            elif action is 'R':
                new_state[x], new_state[x + 1] = new_state[x + 1], new_state[x]
            children.append(Node(new_state, self, action))
        return children

    def get_solution(self):
        solution = []
        solution.append(self.action)
        node = self
        while node.parent != None:
            node = node.parent
            solution.append(node.action)
        solution = solution[:-1]
        solution.reverse()
        return solution


def main():
    root = Node(state, None, None)
    bfs = breadth_first_search(root)
    print('BFS:', bfs)


if __name__ == '__main__':
    main()
