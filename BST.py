from binarytree import Node


def inorderfunction(root):
    if root:
        inorderfunction(root.left)
        print(root.val),
        inorderfunction(root.right)


def postorderfunction(root):
    if root:
        postorderfunction(root.left)
        postorderfunction(root.right)
        print(root.val),


def preorderfunction(root):
    if root:
        print(root.val),
        preorderfunction(root.left)
        preorderfunction(root.right)


root = Node(201)
root.left = Node(200)
root.right = Node(666)
root.left.left = Node(199)
root.right.left = Node(511)
root.right.right = Node(991)
root.left.left.left = Node(1)
root.right.left.left = Node(457)
root.right.left.right = Node(543)
root.right.right.left = Node(764)
root.right.right.right = Node(1001)

print("Sequence for Preorder is:\n")
preorderfunction(root),

print("\nSequence for Inorder is:\n")
inorderfunction(root),

print("\nSequence for Postorder is:\n"),
postorderfunction(root),

print("\t\t\tBINARY SEARCH TREE \n")

print(root)
