
'''
Class definition for a Node of tree. Defines Key, Left, Right, Parent
'''
class BSTNode():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent= None
        self.height = None
    '''
    Prints Tress in the Actual Tree like structure 
    '''
    def _str(self):
        """Internal method for ASCII art."""
        label = str(self.key)
        if self.left is None:
            left_lines, left_pos, left_width = [], 0, 0
        else:
            left_lines, left_pos, left_width = self.left._str()
        if self.right is None:
            right_lines, right_pos, right_width = [], 0, 0
        else:
            right_lines, right_pos, right_width = self.right._str()
        middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
        pos = left_pos + middle // 2
        width = left_pos + middle + right_width - right_pos
        while len(left_lines) < len(right_lines):
            left_lines.append(' ' * left_width)
        while len(right_lines) < len(left_lines):
            right_lines.append(' ' * right_width)
        if (middle - len(label)) % 2 == 1 and self.parent is not None and \
           self is self.parent.left and len(label) < middle:
            label += '.'
        label = label.center(middle, '.')
        if label[0] == '.': label = ' ' + label[1:]
        if label[-1] == '.': label = label[:-1] + ' '
        lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                 ' ' * left_pos + '/' + ' ' * (middle-2) +
                 '\\' + ' ' * (right_width - right_pos)] + \
          [left_line + ' ' * (width - left_width - right_width) + right_line
           for left_line, right_line in zip(left_lines, right_lines)]
        return lines, pos, width

    def __str__(self):
        return '\n'.join(self._str()[0])

class BST():
    def __init__(self):
        self.root = None

    '''
    Insert the Key recursively in the tree.
    '''
    def insertkey(self, key, subtree = None):
        Node = BSTNode(key)

        #One time operation, reserving root node
        if self.root == None:
            self.root = Node

        #Assign Root to Subtree for Navigation deep in the tree
        if subtree == None:
            subtree = self.root

        # Check if left of Subtree has correct location of Node
        if Node.key < subtree.key:
            if subtree.left == None:
                Node.parent = subtree
                subtree.left = Node
            else:
                self.insertNodeRec(key,subtree.left)

        # Check if right of Subtree has correct location of Node
        elif Node.key > subtree.key:
            if subtree.right == None:
                Node.parent = subtree
                subtree.right = Node
            else:
                self.insertNodeRec(Node, subtree.right)

        return Node


    '''
    Insert the Node recursively in the tree.
    '''
    def insertNodeRec(self, Node, subtree = None):
        #One time operation, reserving root node
        if self.root == None:
            self.root = Node

        #Assign Root to Subtree for Navigation deep in the tree
        if subtree == None:
            subtree = self.root

        # Check if left of Subtree has correct location of Node
        if Node.key < subtree.key:
            if subtree.left == None:
                Node.parent = subtree
                subtree.left = Node
            else:
                self.insertNodeRec(Node,subtree.left)

        # Check if right of Subtree has correct location of Node
        elif Node.key > subtree.key:
            if subtree.right == None:
                Node.parent = subtree
                subtree.right = Node
            else:
                self.insertNodeRec(Node, subtree.right)

    '''
    Finds the Unique key if exists, returns the node, None if Key isn't in the tree
    '''
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
    Find the minimum in the given tree
    '''
    def  findMin(self, subtree = None):
        if subtree == None:
            Node = self.root
        else:
            Node = subtree

        while Node.left:
            Node = Node.left

        return Node


    '''
    Find the node to delete from the tree if it exists returns None if Key isn't in the tree or Success
    '''
    def deleteNode(self, key, DelNode = None):

        if DelNode == None:
            Node = self.findkey(key)
            if Node == None:
                return ("Gotcha! Nothing to delete")
        else:
            Node = DelNode

        # Case#1: zero child. Leaf Node
        # Checking if Node is left or right child of its parent, Setting Parents left or right None accordingly
        if Node.left == None and Node.right == None:
            #Node.parent.left = None if Node.parent.left == Node else Node.parent.right = None
            if Node.parent.left == Node:
                Node.parent.left = None
            else:
                Node.parent.right = None

        # Case#2: one child: Left or Right
        elif Node.left == None or Node.right == None:
            if Node == Node.parent.left:
                Node.parent.left = Node.left
            elif Node == Node.parent.right:
                Node.parent.right = Node.right

        # Case#3: 2 childs:  Left and Right
        #Find min in the right subtree, replace the key with Node and delete the replace node.
        # Node.left != None and Node.right != None
        else:
            replaceNode = self.findMin(Node.right)
            Node.key = replaceNode.key
            self.deleteNode(key,replaceNode )


    def __str__(self):
        if self.root is None: return '<empty tree>'
        return str(self.root)

    '''
    Prints the tree in Inorder
    '''

    def inorderTraversal(self, Node=None):
        if Node == None:
            return
        self.inorderTraversal(Node.left)
        print("Node:{}".format(Node.key))
        self.inorderTraversal(Node.right)



'''
Driver Code Ahead
'''

'''
bst = BST()
bst.insertNodeRec(BSTNode(10))
bst.insertNodeRec(BSTNode(20))
bst.insertNodeRec(BSTNode(15))
bst.insertNodeRec(BSTNode(4))
bst.insertNodeRec(BSTNode(2))
bst.insertNodeRec(BSTNode(56))
bst.insertNodeRec(BSTNode(60))
bst.insertNodeRec(BSTNode(40))
Node = bst.insertkey(200)

print (bst)
print (Node)
#bst.inorderTraversal(bst.root)
result = bst.findkey(56)
if result != None:
    print("found")
else:
    print("Better Luck Next time")
'''

#bst.deleteNode(20)
#print (bst)