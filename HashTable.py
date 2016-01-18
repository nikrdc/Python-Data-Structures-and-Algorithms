class HashTable(object):
    def __init__(self, total_buckets=1):
        self.total_buckets = total_buckets
        self.key_list = [None for i in xrange(self.total_buckets)]
        
    def put(self, key, value):
        list_index = hash(key) % self.total_buckets
        if self.key_list[list_index]:
            # handle collision 
            updated = False
            list_length = len(self.key_list[list_index])
            for i in xrange(list_length):
                if self.key_list[list_index][i][0] == key:
                    self.key_list[list_index][i] = (key, value)
                    updated = True
                    break
            if not updated:
                self.key_list[list_index].append((key, value))
        else:
            self.key_list[list_index] = [(key, value)]
    
    def get(self, key):
        list_index = hash(key) % self.total_buckets
        if self.key_list[list_index]:
            for pair in self.key_list[list_index]:
                if pair[0] == key:       
                    return pair[1]
        raise Exception


        