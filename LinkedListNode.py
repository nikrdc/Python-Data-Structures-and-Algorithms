class LinkedListNode(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return str(self.data)

    def has_cycles(self):
        """
        Determine whether the linked list contains a cycle.
        """
        seen = []
        slow_runner = self
        fast_runner = self
        while slow_runner and fast_runner:
            if slow_runner == fast_runner and slow_runner != self:
                return True
            else:
                slow_runner = slow_runner.next
                if fast_runner.next:
                    fast_runner = fast_runner.next.next
                else:
                    fast_runner = None
        return False

    def find_kth(self, k):
        """
        Find the kth to last element of the linked list.
        """
        kth = last = self
        while k > 1:
            last = last.next
            k -= 1
        while last.next:
            kth = kth.next
            last = last.next
        return kth

    def remove_node(self):
        """
        Delete a node in the middle of a singly linked list, given only access 
        to that node. Cannot be the final node of the linked list.
        """
        if self.next:
            self.data = self.next.data
            self.next = self.next.next

    def remove_duplicates(self):
        """
        Remove duplicates from an unsorted linked list without a buffer (in 
        place).
        """
        current = self
        while current:
            penultimate = current
            runner = current.next
            while runner:
                if runner.data == current.data:
                    penultimate.next = runner.next
                else:
                    penultimate = penultimate.next
                runner = runner.next
            current = current.next

    def display(self):
        current = self
        string = ""
        while current:
            string = string + str(current.data) + " "
            current = current.next
        print string


