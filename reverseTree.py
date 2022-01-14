# In this file, we'll create a binary tree and traverse over it using depth-first and breath-first methods.
# Joshua Koshy - koshy.dev - Project Finalized on January 14, 2022

class Tree():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a = Tree("a")
b = Tree("b")
c = Tree("c")
d = Tree("d")
e = Tree("e")
f = Tree("f")
g = Tree("g")
h = Tree("h")
i = Tree("i")
j = Tree("j")
k = Tree("k")
x = Tree("x")
z = Tree("z")

a.left = b      # --------------------------           --------------------------
a.right = c     # |         Tree 1:        |           |    Tree 1 Reversed:    |
b.left = d      # |------------------------|           |------------------------|
b.right = e     # |                        |           |                        |
c.right = f     # |            a           | ---L1-->  |            a           |
d.left = g      # |           / \          | ------->  |           / \          |
d.right = h     # |         b    c         | ---L2-->  |         c    b         |
e.left = i      # |       /   \    \       | ------->  |       /     /  \       |
e.right = j     # |      d     e    f      | ---L3-->  |      f     e    d      |
f.right = k     # |     / \   / \    \     | ------->  |     /     / \   /\     |
j.left = x      # |    g   h  i j     k    | ---L4-->  |    k      j  i h  g    |
j.right = z     # |            / \         | ------->  |          / \           |
                # |           x   z        | ---L5-->  |         z   x          |

def reverseTreeStack(rootNode):
    myList = [rootNode]
    while len(myList) > 0:
        currentVar = myList.pop(0)
        tmp = currentVar.left                    # | ONLY USE IF REVERSING TREE |
        currentVar.left = currentVar.right       # | ONLY USE IF REVERSING TREE |
        currentVar.right = tmp                   # | ONLY USE IF REVERSING TREE |
        print(currentVar.val)
        if currentVar.right is not None:
            myList.insert(0, currentVar.right)
        if currentVar.left is not None:
            myList.insert(0, currentVar.left)

def reverseTreeRecursive(rootNode):
    if rootNode is None:
        return
    print(rootNode.val)
    tmp = rootNode.left                        # | ONLY USE IF REVERSING TREE |
    rootNode.left = rootNode.right             # | ONLY USE IF REVERSING TREE |
    rootNode.right = tmp                       # | ONLY USE IF REVERSING TREE |
    reverseTreeRecursive(rootNode.left)
    reverseTreeRecursive(rootNode.right)
