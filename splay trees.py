inp = open("abce.in", "r")
out = open("abce.out", "w")

class Node:
    """setters"""
    def __init__(self, data):
        self.data = data
        self.par = None
        self.left = None
        self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        node = Node(key)
        y = None
        x = self.root

        while x != None:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.par = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node
        self.splay(node)

    def find_function(self, node, key):
        if node == None or key == node.data:
            return node

        if key < node.data:
            return self.find_function(node.left, key)
        return self.find_function(node.right, key)

    def find_node(self, k):
        x = self.find_function(self.root, k)
        if x != None:
            self.splay(x)
            return x
        else:
            return None

    def find(self, x):
        if self.find_node(x):
            out.write(str(1) + "\n")
        else:
            out.write(str(0) + "\n")

    def delete_function(self, node, key):
        x = None
        tree1 = None
        tree2 = None
        while node != None:
            if node.data == key:
                x = node

            if node.data <= key:
                node = node.right
            else:
                node = node.left

        if x == None:
            return

        self.splay(x)
        if x.right != None:
            tree1 = x.right
            tree1.par = None
        else:
            tree1 = None

        tree2 = x
        tree2.right = None
        x = None

        if tree2.left != None:
            tree2.left.par = None

        self.root = self.join(tree2.left, tree1)
        tree2 = None

    def delete(self, data):
        self.delete_function(self.root, data)

    def rotateL(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.par = x

        y.par = x.par
        if x.par == None:
            self.root = y
        elif x == x.par.left:
            x.par.left = y
        else:
            x.par.right = y
        y.left = x
        x.par = y

    def rotateR(self, x):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.par = x

        y.par = x.par;
        if x.par == None:
            self.root = y
        elif x == x.par.right:
            x.par.right = y
        else:
            x.par.left = y

        y.right = x
        x.par = y

    def splay(self, x):
        while x.par != None:
            if x.par.par == None:
                if x == x.par.left:
                    self.rotateR(x.par)
                else:
                    self.rotateL(x.par)
            elif x == x.par.left and x.par == x.par.par.left:
                self.rotateR(x.par.par)
                self.rotateR(x.par)  # zig - zig right
            elif x == x.par.right and x.par == x.par.par.right:
                self.rotateL(x.par.par)
                self.rotateL(x.par) # zig - zig left
            elif x == x.par.right and x.par == x.par.par.left:
                self.rotateL(x.par)
                self.rotateR(x.par)  # zig- zag
            else:
                self.rotateR(x.par)
                self.rotateL(x.par)  # zig - zag


    def successor(self, x):
        """Keeps searching until a higher value than X pops up in the splay tree"""
        while self.find_node(x) == None:
            x += 1
            if x > 1000000000:
                return -1
        out.write(str(x) + "\n")



    def predecessor(self, x):
        """Keeps searching until a lower value than X pops up in the splay tree"""
        while self.find_node(x) == None:
            x -= 1
            if x < -1000000000:
                return -1
        out.write(str(x) + "\n")


    def maximum(self, node):
        """Keeps going to the right until searching the higher value"""
        while node.right != None:
            node = node.right
        return node


    def join(self, Ltree, Rtree):
        """Splay the largest key in the left subtree, then make rSub the right child of lSub"""
        if Ltree == None:
            return Rtree

        if Rtree == None:
            return Ltree

        x = self.maximum(Ltree)
        self.splay(x)
        x.right = Rtree
        Rtree.par = x
        return x


    def interval(self, x, y):
        for i in range(x + 1, y):
            if self.find_node(i) != None:
                out.write(str(i) + " ")
        out.write("\n")

ST = SplayTree()
Q = int(inp.readline())
switcher = {
    "1":ST.insert,
    "2":ST.delete,
    "3":ST.find,
    "4":ST.predecessor,
    "5":ST.successor,
    "6":ST.interval
}

for operation in inp.readlines():
    if operation[0] in ("1", "2", "3", "4", "5"):
        switcher[operation[0]](int(operation[2:]))
    else:
       switcher[operation[0]](int(operation[2:operation.find(" ", 2)]), int(operation[operation.find(" ", 2):]))



