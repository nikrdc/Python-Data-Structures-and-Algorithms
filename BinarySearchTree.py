class BSTNode:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None


class BinarySearchTree(object):
    """
    Binary Search Tree represented using BSTNodes.
    """
    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        Insert a value into the BinarySearchTree as a leaf BSTNode.
        """
        # If tree is empty, add value as root
        if not self.root:
            self.root = BSTNode(value)
        else:
            current_node = self.root
            while current_node:
                if value <= current_node.value:
                    if current_node.left_child:
                        current_node = current_node.left_child
                    else:
                        current_node.left_child = BSTNode(value)
                        current_node.left_child.parent = current_node
                        break
                else:
                    if current_node.right_child:
                        current_node = current_node.right_child
                    else:
                        current_node.right_child = BSTNode(value)
                        current_node.right_child.parent = current_node
                        break

    def find(self, value):
        """
        Use the inherent structure of the BinarySearchTree to find a value,
        starting from the root. 
        """
        if not self.root:
            return None
        else:
            current_node = self.root
            while value != current_node.value:
                if value < current_node.value:
                    if current_node.left_child:
                        current_node = current_node.left_child
                    else:
                        return None
                else:
                    if current_node.right_child:
                        current_node = current_node.right_child
                    else:
                        return None
            return current_node

    def remove(self, value):
        """
        Remove a value from the BinarySearchTree by deleting its BSTNode and 
        rearranging the remanining nodes. 
        """
        removenode = self.find(value)
        if not removenode:
            return "value not found in BinarySearchTree"

        if removenode.left_child and removenode.right_child:
            # both children present
            smallest = removenode.right_child
            while smallest.left_child:
                smallest = smallest.left_child
            removenode.value = smallest.value
            if smallest.right_child:
                smallest.parent.left_child = smallest.right_child

        elif removenode.left_child:
            # only left child present
            if removenode == removenode.parent.left_child:
                removenode.parent.left_child = removenode.left_child
            else:
                removenode.parent.right_child = removenode.left_child

        elif removenode.right_child:
            # only right child present
            if removenode == removenode.parent.left_child:
                removenode.parent.left_child = removenode.right_child
            else:
                removenode.parent.right_child = removenode.right_child

    def dfs(self):
        """
        Depth first search that traverses a BinarySearchTree. Uses the 
        inner_dfs function to recursively traverse the tree from the root.
        """
        def inner_dfs(node):
            # preorder visit
            if node.left_child:
                inner_dfs(node.left_child)
            # inorder visit
            print node.value
            if node.right_child:
                inner_dfs(node.right_child)
            # postorder visit
        return inner_dfs(self.root)

    def bfs(self):
        """
        Breadth first search that traverses a BinarySearchTree. Uses a Python 
        list as a queue for traversing nodes by distance from the root. 
        """
        queue = []
        queue.append(self.root)
        while queue:
            node = queue[0]
            print node.value
            if node.left_child:
                queue.append(node.left_child)
            if node.right_child:
                queue.append(node.right_child)
            del queue[0]

    def superbalanced(self):
        """
        A tree is "superbalanced" if the difference between the depths of any 
        two leaf nodes is no greater than one.
        """
        self.min_depth = None
        self.max_depth = None

        queue = []
        queue.append((self.root, 0))
        while queue:
            node = queue[0][0]
            depth = queue[0][1]
            if node.left_child:
                queue.append((node.left_child, depth+1))
            if node.right_child:
                queue.append((node.right_child, depth+1))
            if not node.left_child and not node.right_child:
                if self.min_depth:
                    if self.max_depth:
                        if depth < self.min_depth or depth > self.max_depth:
                            return False
                    elif abs(self.min_depth - depth) <= 1:
                        if self.min_depth > depth:
                            self.max_depth = self.min_depth
                            self.min_depth = depth
                        elif self.min_depth < depth:
                            self.max_depth = depth
                    else:
                        return False
                else:
                    self.min_depth = depth
            del queue[0]

        return True

    def valid(self):
        """
        Check that a binary tree is a valid binary search tree.
        """
        queue = []
        queue.append(self.root)
        while queue:
            node = queue[0]
            if node.left_child:
                if node.left_child.value <= node.value:
                    queue.append(node.left_child)
                else:
                    return False
            if node.right_child:
                if node.right_child.value > node.value:
                    queue.append(node.right_child)
                else:
                    return False
            del queue[0]
        return True




