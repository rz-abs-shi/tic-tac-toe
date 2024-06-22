class Node:
    def __init__(self, key: str, data: dict = None):
        self.key = key
        self.children = {}
        self.data = data

    def __str__(self):
        return f'key={self.key} [children: {len(self.children)}]'

    def __repr__(self):
        return str(self)

    def add_child(self, key, data: dict = None):
        node = Node(key, data)
        self.children[key] = node
        return node
