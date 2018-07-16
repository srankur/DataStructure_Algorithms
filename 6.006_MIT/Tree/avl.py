from BST import BST

def height(Node):
    if Node == None:
        return -1
    else:
        return Node.height

def update_height(Node):
    Node.height = max(height(Node.left), height(Node.right)) +1


class AVL(BST):

    def leftRotate(self,Node):
        y = Node.right
        y.parent = Node.parent

        # Manage the Node's relation with its existing parent.
        #Case#1: Parent of node is None, Set the Node as Root.
        if y.parent == None:
            self.root = y
        # Case#2: Node was left child of its parent, Set the Y as left child.
        elif y.parent.left == Node:
            y.parent.left = y
        # Case#3: Node was righ child of its parent, Set the Y as right child.
        elif y.parent.right == Node:
            y.parent.right = y

        #Manage the left child of Y, since its Min in the right subtree of Node, will set on Right to Node.Set itself
        # as parent of right child
        Node.right = y.left
        if Node.right != None:
            Node.right.parent = Node

        #Finally delink Node and set it on left of Y
        y.left = Node
        Node.parent = y

        update_height(Node)
        update_height(y)



    def rightRotate(self,Node):
        y = Node.left
        y.parent = Node.parent

        # Manage the Node's relation with its existing parent.
        # Case#1: Parent of node is None, Set the Node as Root.
        if y.parent == None:
            self.root = y
        # Case#2: Node was left child of its parent, Set the Y as left child.
        elif y.parent.left == Node:
            y.parent.left = y
        # Case#3: Node was righ child of its parent, Set the Y as right child.
        elif y.parent.right == Node:
            y.parent.right = y

        # Manage the right child of Y, since its Max in the left subtree of Node, will set on left to Node.Set itself
        # as parent of left child
        Node.left = y.right
        if Node.left != None:
            Node.left.parent = Node

        # Finally delink Node and set it on left of Y
        y.right = Node
        Node.parent = y

        update_height(Node)
        update_height(y)


    def rebalance(self, Node):
        while Node != None:
            update_height(Node)
            if height(Node.left)>= 2 + height(Node.right):
                if height(Node.left.left) >= height(Node.left.right):
                    self.rightRotate(Node)
                else:
                    self.leftRotate(Node.left)
                    self.rightRotate(Node)
            if height(Node.right) >= 2 + height(Node.left):
                if height(Node.right.right) >= height(Node.right.left):
                    self.leftRotate(Node)
                else:
                    self.rightRotate(Node.right)
                    self.leftRotate(Node)
            Node = Node.parent

    def insert(self, key):
        Node = super(AVL,self).insertkey(key)
        self.rebalance(Node)






avl= AVL()
avl.insert(10)
avl.insert(20)
print (avl, '\n',"----------------" )
avl.insert(30)
print (avl, '\n',"----------------" )
avl.insert(35)
print (avl, '\n',"----------------" )
#avl.insert(2)
avl.insert(56)
print (avl, '\n',"----------------" )
avl.insert(60)
print (avl, '\n',"----------------" )
avl.insert(40)
print (avl, '\n',"----------------" )
avl.insert(200)
print (avl, '\n',"----------------" )
avl.insert(215)
print (avl, '\n',"----------------" )