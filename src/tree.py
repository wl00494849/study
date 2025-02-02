class Decision_Tree:
    def __init__(self):
        self.root = None

class Node:
    def __init__(self, data,func):
        self.data = data
        self.func = func
        self.left = None
        self.right = None