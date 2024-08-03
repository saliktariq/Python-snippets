import json
import random

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def to_json(self):
        """Converts the tree to a nested dictionary suitable for JSON."""
        data = {str(self.val): {}}
        if self.left:
            data[str(self.val)]["left"] = self.left.to_json()
        if self.right:
            data[str(self.val)]["right"] = self.right.to_json()
        return data
    def __str__(self, level=0):
        return json.dumps(self.to_json(), indent=2)

def generate_random_bst(depth, min_val=0, max_val=100, full_prob=0.8):
    """
    Generates a random BST of given depth with values
    between min_val and max_val.
    """

    if depth == 0:
        return None

    root_val = random.randint(min_val, max_val)
    root = Node(root_val)

    create_full_node = random.random() < full_prob

    if create_full_node and min_val < root_val:
        root.left = generate_random_bst(depth - 1, min_val, root_val - 1, full_prob)
    elif min_val < root_val:
        root.left = generate_random_bst(depth - 1, min_val, root_val - 1, full_prob=0)  # Force empty children

    if create_full_node and root_val < max_val:
        root.right = generate_random_bst(depth - 1, root_val + 1, max_val, full_prob)
    elif root_val < max_val:
        root.right = generate_random_bst(depth - 1, root_val + 1, max_val, full_prob=0)  # Force empty children

    return root
