class Node:
    def __init__(self, key: int) -> None:
        self.key: int = key
        self.left: Node = None
        self.right: Node = None

    def child_count(self) -> int:
        c = 0
        if self.left != None: c += 1
        if self.right != None: c += 1
        return c

    def get_only_child_direction(self) -> str:
        if self.child_count() != 1:
            raise Exception("Cannot get only child direction when there are " + str(self.child_count()) + " children")
        
        if self.left != None:
            return "left"
        else:
            return "right"

    def has(self, direction: str) -> bool:
        if direction == "left":
            return self.left != None
        elif direction == "right":
            return self.right != None
        else:
            return False

    def __str__(self) -> str:
        return f"{self.key} with {self.child_count()} children"

    def __repr__(self) -> str:
        return f"{self.key} with {self.child_count()} children"

class BinaryTree:
    def __init__(self, root: Node) -> None:
        self.root = root

    def add(self) -> None:
        pass

    def size(self) -> int:
        pass

    def depth(self) -> int:
        pass

    def full_traverse(self):
        self._traverse(self.root)

    def _traverse(self, start: Node):
        pass

    def to_str(self) -> str:
        return "Root: " + str(self.root)

    def __str__(self) -> str:
        return self.to_str()

    def __repr__(self) -> str:
        return self.to_str()