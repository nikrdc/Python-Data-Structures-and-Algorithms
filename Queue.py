class Queue(object):
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, data):
        new = LinkedListNode(data)
        if self.last:
            self.last.next = new
            self.last = new
        else:
            self.first = self.last = new

    def dequeue(self):
        if self.first:
            retval = self.first.data
            if self.first == self.last:
                self.last = None
            self.first = self.first.next
            return retval
        return None


        