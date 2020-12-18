

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return self.val

def maketree(line):
    return line


def evaluate_tree(tree):
    return 0

with open("day18test.txt", "r") as f:
    for line in f:
        tree = maketree(line)

evaluate_tree(tree)