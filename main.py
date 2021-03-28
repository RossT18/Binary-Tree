import BinaryTree as bt

# https://upload.wikimedia.org/wikipedia/commons/d/da/Binary_search_tree.svg

root = bt.Node(8)

root.left = bt.Node(3)
root.left.left = bt.Node(1)
root.left.right = bt.Node(6)

root.left.right.left = bt.Node(4)
root.left.right.right = bt.Node(7)

root.right = bt.Node(10)
root.right.right = bt.Node(14)
root.right.right.left = bt.Node(13)

# Expected output order:
# 1,3,4,6,7,8,10,13,14

tree = bt.BinaryTree(root)

print(tree)

tree.print_tree()

print(len(tree))

#print("Size:", tree.size())