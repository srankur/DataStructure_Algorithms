class DisjointSets():
    def MakeSet(node):
        node.parent = node
        node.rank = 0
        print(node.parent)
        print(node.rank)


    def find(node):
        if node.parent == node:
            return node
        else:
            node.parent = DisjointSets.find(node.parent)
            node.parent

    def union(node_x,node_y):
        x_root = DisjointSets.find(node_x)
        y_root = DisjointSets.find(node_y)

        if x_root.rank > y_root.rank:
            y_root.parent = x_root
        elif x_root.rank < y_root.rank:
            x_root.parent = y_root
        elif x_root != y_root:
            y_root.parent = x_root
            x_root.rank += 1

