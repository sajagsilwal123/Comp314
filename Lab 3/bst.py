class BinarySearchTree:

    def __init__(self):
        self._size = 0
        self.root = None    

    class Node:
        def __init__(self,key,value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None

    def size(self):
        return self._size
    
    def add(self,key,value):
        if self.root == None:
            self.root = self.Node(key, value)
            self._size += 1
        else:
            self.addRec(self.root,key,value)
                 
    def addRec(self,subtree:Node,key,value):

        if subtree.key > key:
            if subtree.left == None:
                subtree.left = self.Node(key,value)
                self._size += 1
            else:
                self.addRec(subtree.left,key,value)
        elif subtree.key < key:
            if subtree.right == None:
                subtree.right = self.Node(key,value)
                self._size += 1
            else:
                self.addRec(subtree.right,key,value)
        
    
    def search(self, key):
        return self.search_recursion(self.root,key)

    def search_recursion(self, subtree:Node, key):
        if subtree == None:
            return False
        elif subtree.key == key:
            return subtree.value
        elif subtree.key < key:
            return self.search_recursion(subtree.right,key)
        else:
            return self.search_recursion(subtree.left,key)

    def inorder_walk(self):
        visited_node = []
        self.inorder_walkRec(self.root, visited_node)
        return visited_node

    def inorder_walkRec(self,subtree:Node,visited_node):
        if subtree:
            self.inorder_walkRec(subtree.left,visited_node)
            visited_node.append(subtree.key)
            self.inorder_walkRec(subtree.right,visited_node)
    
    def preorder_walk(self):
        visited_node = []
        self.preorder_walkRec(self.root, visited_node)
        return visited_node

    def preorder_walkRec(self,subtree:Node,visited_node):
        if subtree:
            visited_node.append(subtree.key)
            self.preorder_walkRec(subtree.left,visited_node)
            self.preorder_walkRec(subtree.right,visited_node)

    def postorder_walk(self):
        visited_node = []
        self.postorder_walkRec(self.root, visited_node)
        return visited_node

    def postorder_walkRec(self,subtree:Node,visited_node):
        if subtree:
            self.postorder_walkRec(subtree.left,visited_node)
            self.postorder_walkRec(subtree.right,visited_node)
            visited_node.append(subtree.key)

    def smallest(self):
        return self.smallestRec(self.root)

    def smallestRec(self,subtree:Node):
        if subtree.left == None:
            return (subtree.key, subtree.value)
        else:
            return self.smallestRec(subtree.left)

    def largest(self):
        return self.largestRec(self.root)

    def largestRec(self,subtree:Node):
        if subtree.right == None:
            return (subtree.key, subtree.value)
        else:
            return self.largestRec(subtree.right)

    def remove(self, key):
        if self.search(key):
            self.root = self.removeRec(self.root, key)
            self._size -= 1
        else:
            return self.search(key)

    def removeRec(self, subtree, key):
        if subtree is None:
            return subtree
        elif key < subtree.key:
            subtree.left = self.removeRec(subtree.left, key)
            return subtree
        elif key > subtree.key:
            subtree.right = self.removeRec(subtree.right, key)
            return subtree
        else:
            if subtree.left is None and subtree.right is None:
                return None
            elif subtree.left is None or subtree.right is None:
                if subtree.left is not None:
                    return subtree.left
                else:
                    return subtree.right
            else:
                successor = self.largestRec(subtree.left)
                subtree.key = successor[0]
                subtree.value = successor[1]
                subtree.left = self.removeRec(subtree.left, successor[0])
                return subtree



