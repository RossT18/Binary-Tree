import BinaryTree as bt

# https://upload.wikimedia.org/wikipedia/commons/d/da/Binary_search_tree.svg

root = bt.Node(8)

tree = bt.BinaryTree(root)

tree.add(3)
tree.add(1)
tree.add(6)
tree.add(4)
tree.add(7)
tree.add(10)
tree.add(14)
tree.add(13)

# Expected output order:
# 1,3,4,6,7,8,10,13,14

print(tree)

print("Length: " + str(len(tree)))