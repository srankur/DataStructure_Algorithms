class BSTNode():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST():
    def __init__(self):
        self.root = None

    def insertNodeRec(self, Node, subtree = None):
        #One time operation, reserving root node
        if self.root == None:
            self.root = Node

        #
        if subtree == None:
            subtree = self.root

        if Node.key < subtree.key:
            if subtree.left == None:
                subtree.left = Node
            else:
                self.insertNodeRec(Node,subtree.left)
        elif Node.key > subtree.key:
            if subtree.right == None:
                subtree.right = Node
            else:
                self.insertNodeRec(Node, subtree.right)

    def deleteNode(self):
        pass

    """
    Finds the Unique key if exists, returns the node, None if Key isn't in the tree 
    """
    def findkey(self, key, root =None):
        if (root == None):
            root = self.root

        if root.key == key:
            return root

        if key < root.key:
            if root.left == None:
                return None
            else:
                return self.findkey(key, root.left)
        elif key > root.key:
            if root.right == None:
                return None
            else:
                return self.findkey(key, root.right)



    '''
    Prints the tree in Inorder
    '''
    def inorderTraversal(self, Node=None):
        if Node == None:
            return
        self.inorderTraversal(Node.left)
        print("Node:{}".format(Node.key))
        self.inorderTraversal(Node.right)


bst = BST()
bst.insertNodeRec(BSTNode(10))
bst.insertNodeRec(BSTNode(20))
bst.insertNodeRec(BSTNode(4))
bst.insertNodeRec(BSTNode(56))

bst.inorderTraversal(bst.root)
result = bst.findkey(56)
if result != None:
    print("found")
else:
    print("Better Luck Next time")