
from collections import deque



class BinaryNode():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

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



class BinaryTree():
    def __init__(self ):
        self.root = None

    '''
    Node insertion, Find place of insertion using the logic BFS traversal  
    '''

    def insertNode(self, Node, subtree = None):
        if self.root is None:
            self.root = Node
            return
        else:
            q = deque()
            q.append(self.root)
            while q is not None:
                subtree = q.popleft()
                if subtree.left is not None:
                    q.append(subtree.left)
                elif subtree.left is None:
                    subtree.left = Node
                    Node.parent = subtree
                    #q.clear()
                    break
                if subtree.right is not None:
                    q.append(subtree.right)
                elif subtree.right is None:
                    subtree.right = Node
                    Node.parent = subtree
                    #q.clear()
                    break

    '''
    BFS traversal  ## FIX this 
    '''

    def breadthfirstsearch(self):
        if self.root is None:
            return
        else:
            q= deque()
            q.append(self.root)
            while q is not None:
                node = q.popleft()
                print(node.key)
                if node.left is not None:
                    q.append(node.left)
                elif node.right is not None:
                    q.append(node.right)

    '''
    Finds Lowest common Ancestor for the given two keys 
    
    '''
    def lowest_common_ancestor_optimized(self, key1, key2, subtree = None):

        #Optional Logic to check if both the keys were found
        key1Found = False
        key2Found = False
        lcaFound = False

        if subtree is None:
            return

        if subtree.key == key1:
            key1Found = True
            return subtree
        elif subtree.key == key2:
            key2Found = True
            return subtree

        print("Current Status Key1:{}-Key2:{}".format(key1Found, key2Found))

        left = self.lowest_common_ancestor(key1, key2, subtree.left)
        right = self.lowest_common_ancestor(key1, key2, subtree.right)

        if left is not None and right is not None:
            ##OPtionaLogic
            lcaFound = True
            print("LCA Found:{}".format(subtree.key))
            ##OPtionaLogic
            return subtree
        if left is None and right is None:
            return None
        if left is not None:
            return left
        elif right is not None:
            return right


    def lowest_common_ancestor(self, key1, key2, subtree = None):

        if subtree is None:
            return
        if subtree.key == key1 or subtree.key == key2:
            return subtree

        left = self.lowest_common_ancestor(key1, key2, subtree.left)
        right = self.lowest_common_ancestor(key1, key2, subtree.right)

        if left is not None and right is not None:
            return subtree
        if left is None and right is None:
            return None
        if left is not None:
            return left
        elif right is not None:
            return right

    def size(self, tree):
        if tree is None:
            return 0
        else:
            return (self.size(tree.left) + self.size(tree.right) +1)


    def maxdepth(self, tree):
        if tree is None:
            return 0
        else:
            ldepth = self.maxdepth(tree.left)
            rdepth = self.maxdepth(tree.right)

            if ldepth > rdepth:
                return ldepth +1
            else:
                return rdepth+1

    def tree_mirror(self,tree):
        if tree is None:
            return
        else:
            self.tree_mirror(tree.left)
            self.tree_mirror(tree.right)
        tree.left,tree.right = tree.right, tree.left



    #Add Path to this
    def has_path_sum(self,tree,sum,path):
        if tree is None:
            return (False)
        if tree.key == sum and tree.left is None and tree.right is None:
            path.append(tree.key)
            return (True)
        else:
            #return (self.has_path_sum(tree.left, sum-tree.key) or  self.has_path_sum(tree.right, sum-tree.key))
            if self.has_path_sum(tree.left, sum-tree.key,path):
                path.append(tree.key)
                return True
            if self.has_path_sum(tree.right, sum-tree.key, path):
                path.append(tree.key)
                return True
            else:
                return False


    def __str__(self):
        if self.root is None: return '<empty tree>'
        return str(self.root)



bintree = BinaryTree()
bintree.insertNode(BinaryNode(1))
bintree.insertNode(BinaryNode(2))
bintree.insertNode(BinaryNode(3))
bintree.insertNode(BinaryNode(4))
bintree.insertNode(BinaryNode(5))
bintree.insertNode(BinaryNode(6))
bintree.insertNode(BinaryNode(7))
bintree.insertNode(BinaryNode(8))
bintree.insertNode(BinaryNode(9))
bintree.insertNode(BinaryNode(10))
bintree.insertNode(BinaryNode(11))
bintree.insertNode(BinaryNode(12))

'''
lca = bintree.lowest_common_ancestor_optimized(8,12, bintree.root)
print("The LCA for 8,12 is {}".format(lca.key))

lca = bintree.lowest_common_ancestor_optimized(8,5, bintree.root)
print("The LCA for 8,5 is {}".format(lca.key))

lca = bintree.lowest_common_ancestor_optimized(2,4, bintree.root)
print("The LCA for 4,2 is {}".format(lca.key))

lca = bintree.lowest_common_ancestor_optimized(7,12, bintree.root)
print("The LCA for 7,12 is {}".format(lca.key))


print("Size of the tree is: {}".format(bintree.size(bintree.root)))
print("depth of the tree is: {}".format(bintree.maxdepth(bintree.root)))
'''
path =[]
res = bintree.has_path_sum(bintree.root, 19,path)
print ("result:{}".format(res))
print(path[::-1])
'''
bintree.tree_mirror(bintree.root)
print(bintree)
'''




#bintree.breadthfirstsearch()
#print (bintree)

