class Node:
    left = None
    key = 0
    right = None
    def __init__(self, key, value):
       self.key = key
       self.value=value

class BinarySearchTree():
    def __init__(self):
        self.root = None

    
    def add(self, key, value):
      
        if not self.root:
            self.root = Node(key, value)
            return
        curr = self.root
        while True:
            if key < curr.key:
                if not curr.left:
                    curr.left = Node(key, value)
                    break
                else:
                    curr = curr.left
            else:
                if not curr.right:
                    curr.right = Node(key,value)
                    break
                else:
                    curr = curr.right

    def search(self,key):
       curr = self.root
       while curr:
           if curr.key == key:
               return curr.value
           elif key < curr.key:
               curr = curr.left
           else:
               curr = curr.right
       return False
      
    def inorder_walk(self):
        stack = []
        l = []
        node = self.root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                l.append((node.key))
                node = node.right
        return l
    def preorder_walk(self):
        if self.root is None:
            return []

        stack = [self.root]
        l = []

        while stack:
            node = stack.pop()
            l.append(node.key)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return l
    def postorder_walk(self):
        if self.root is None:
            return []
        stack = [self.root]
        l = []
        node = self.root
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            l.append(node.key)

        return l[::-1]
   
  
    def size(self):
        a=[]
        a = self.inorder_walk()
        return len(a)

    def smallest(self):
       curr = self.root
       while curr.left:
           curr = curr.left
       return (curr.key,curr.value)
    def largest(self):
       curr = self.root
       while curr.right:
           curr=curr.right
       return (curr.key,curr.value)
   
    def remove(self, key):
        parent = None
        node = self.root

        while node  and node.key != key:
            parent = node
            if key < node.key:
                node = node.left
            else:
                node = node.right

        if node is None:
            return False

        if node.left is None:
            if parent is None:
                self.root = node.right
            elif node == parent.left:
                parent.left = node.right
            else:
                parent.right = node.right
        elif node.right is None:
            if parent is None:
                self.root = node.left
            elif node == parent.left:
                parent.left = node.left
            else:
                parent.right = node.left
        else:
            successor = node.left
            while successor.right is not None:
                successor_parent = successor
                successor = successor.right

            if node == self.root:
                self.root = successor
            elif node == parent.right:
                parent.right = successor
            else:
                parent.left = successor

            successor.right = node.right

            if successor != node.left:
                successor_parent.right = successor.left
                successor.left = node.left

        
        return True