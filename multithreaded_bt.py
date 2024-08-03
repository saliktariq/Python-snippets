import threading
from queue import Queue

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def threaded_bt_search(root, target, found_flag, found_queue):
    if not root or found_flag.is_set():
        return

    if root.val == target:
        found_flag.set()
        found_queue.put(root)
        return

    # Launch concurrent threads for left and right subtrees
    left_thread = threading.Thread(target=threaded_bt_search,
                                   args=(root.left, target, found_flag, found_queue))
    right_thread = threading.Thread(target=threaded_bt_search,
                                    args=(root.right, target, found_flag, found_queue))

    left_thread.start()
    right_thread.start()

    left_thread.join()
    right_thread.join()
