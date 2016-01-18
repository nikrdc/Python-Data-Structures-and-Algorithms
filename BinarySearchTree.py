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


