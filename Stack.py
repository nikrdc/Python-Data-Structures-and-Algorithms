class Stack(object):
    def __init__(self):
        self.top = None
        self.height = 0

    def pop(self):
        if self.top:
            retval = self.top.data
            self.top = self.top.next
            self.height -= 1
            return retval
        return None

    def push(self, data):
        n = LinkedListNode(data)
        n.next = self.top
        if self.top:
            if data < self.top.minval:
                n.minval = data
            else:
                n.minval = self.top.minval
        else:
            n.minval = data
        self.height += 1
        self.top = n

    def peek(self):
        if self.top:
            return self.top.data
        return None

    def getmin(self):
        if self.top:
            return self.top.minval
        return None


class StackOfStacks(object):
    def __init__(self, maxheight):
        self.maxheight = maxheight
        self.stacklist = []

    def push(self, data):
        if len(self.stacklist) == 0 or self.stacklist[-1].height == self.maxheight:
            new_stack = Stack()
            self.stacklist.append(new_stack)
            new_stack.push(data)
        else:
            self.stacklist[-1].push(data)

    def pop(self):
        retval = self.stacklist[-1].pop()
        if self.stacklist[-1].height == 0:
            del self.stacklist[-1]
        return retval

    def peek(self):
        return self.stacklist[-1].peek()

    def popat(self, index):
        if len(self.stacklist) <= index:
            return "ERROR"
        return self.stacklist[index].pop()


        