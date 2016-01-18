class PriorityQueue(object):
    """ 
    Priority queue represented by a heap (max or min), which is implemented by a binary tree,
    which is represented by a list. 
    For each element of the list with index i, its children are at indices 2*i and (2*i)+1 and 
    its parent is at index i/2.
    Currently does not handle in order dequeuing of duplicate priorities.
    """

    def __init__(self, kind):
        if kind == "min" or kind == "max":
            self.kind = kind
        else:
            print "invalid type"
            # raise exception
        self.binary_tree = [None] # First element unused

    def less_than(self, a, b):
        return a < b
        
    def greater_than(self, a, b):
        return a > b

    def enqueue(self, priority, value):
        # Add (priority, value) tuple to end of binary tree
        self.binary_tree.append((priority, value))

        # Bubble up tuple while parent priority < node priority
        i = len(self.binary_tree) - 1

        if self.kind == "max":
            comparator = self.less_than
        else:
            comparator = self.greater_than

        while (i/2 != 0) and comparator(self.binary_tree[i/2][0], self.binary_tree[i][0]):
            node = self.binary_tree[i]
            self.binary_tree[i] = self.binary_tree[i/2]
            self.binary_tree[i/2] = node
            i = i/2

    def dequeue(self):
        if len(self.binary_tree) == 1:
            print "PriorityQueue empty"
            # raise exception

        retnode = self.binary_tree[1]

        # Replace root with last node in binary tree
        last = self.binary_tree[-1]
        self.binary_tree[1] = last
        del self.binary_tree[-1]

        # Bubble down new root until it is larger than its children
        i = 1

        if self.kind == "max":
            comparator = self.less_than
        else:
            comparator = self.greater_than

        while 2*i < len(self.binary_tree):
            if 2*i+1 == len(self.binary_tree):
                if comparator(self.binary_tree[i][0], self.binary_tree[2*i][0]):
                    relevant_child = 2*i
                else:
                    break
            else:
                if (comparator(self.binary_tree[i][0],self.binary_tree[2*i][0]) or 
                    comparator(self.binary_tree[i][0], self.binary_tree[2*i+1][0])):
                    if comparator(self.binary_tree[2*i+1][0], self.binary_tree[2*i][0]):
                        relevant_child = 2*i
                    else:
                        relevant_child = 2*i+1
                else:
                    break
            node = self.binary_tree[i]
            self.binary_tree[i] = self.binary_tree[relevant_child]
            self.binary_tree[relevant_child] = node
            i = relevant_child

        return retnode


 
