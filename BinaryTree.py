class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def __str__(self):
      print("Value is {}. Left is {}. Right is {}.".format(self.value, self.left, self.right))

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.post_order_print(tree.root, "")
        else:
            print("Traversal type {0} is not supported".format(traversal_type))
            return False

    def preorder_print(self, start, traversal):
        # Root -> left -> rig`ht
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        # Let -> Root -> Right
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def post_order_print(self, start, traversal):
        # Let -> root -> Right
        if start:
            traversal = self.post_order_print(start.left, traversal)
            traversal = self.post_order_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal
    def add(self, start, add_item):
        add_item_node = Node(add_item)
        if start.left == None and add_item_node.value < start.value:
            start.left = add_item_node
            return
        elif start.right == None and add_item_node.value > start.value:
            start.right = add_item_node
            return
        else:
            if (add_item_node.value < start.value):
                self.add(start.left, add_item)
            else:
                self.add(start.right, add_item)
    def check_element(self, start, target):
        if start == None:
            return False
        elif target.value == start.value:
            return True
        elif target.value < start.value:
            return self.check_element(start.left, target)
        else:
            return self.check_element(start.right, target)

    
#               12
#           /       \
#          9         13
#         / \       /  \
#        6   10   11    14
#         \         \      \
#          7        12.5    15

#               8
#           /       \
#          3         10
#         / \         \
#        1   6         14
#                      / 
#                    13


#               1
#           /       \  
#          2          3  
#         /  \      /   \
#        4    5     6   7 

# Pre-order: 1-2-4-5-3-6-7-
# Inorder: 4-2-5-1-6-3-7
# Post-order: 4-2-5-6-3-7-1

# Set up tree:

tree = BinaryTree(8)
# print(tree.root.value)
tree.root.left = Node(3)
tree.root.right = Node(10)

tree.root.left.left = Node(1)
tree.root.left.right = Node(6)

tree.root.right.right = Node(14)
tree.root.right.right.left = Node(13)

tree.add(tree.root, 7)
tree.add(tree.root, 15)

print(tree.preorder_print(tree.root, "preorder"))
print(tree.check_element(tree.root, Node(15)))