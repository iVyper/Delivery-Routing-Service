class HashTable:
    '''
    A simple hash table implementation for storing packages.
    The table is implemented as a list of lists (buckets) to handle collisions.
    '''
    def __init__(self, size):
        # Create a list of empty buckets with the given size.
        self.table = []
        for i in range(size):
            self.table.append([])

    '''
    Inserts an item into the hash table using a hash function.
    If an item with the same key already exists, it is replaced.
    Returns True upon successful insertion.
    '''
    def insert(self, key, item):
        index = hash(key) % len(self.table)
        index_list = self.table[index]
        # Check if the key already exists in the bucket; if so, update it.
        for key_val in index_list:
            if key_val[0] == key:
                key_val[1] = item
                return True
        # If not found, create a new key-value pair and append it.
        key_value = [key, item]
        index_list.append(key_value)
        return True

    '''
    Retrieves an item from the hash table by its key.
    Returns the item if found, otherwise None.
    '''
    def lookup(self, key):
        index = hash(key) % len(self.table)
        index_list = self.table[index]
        for key_val in index_list:
            if key_val[0] == key:
                return key_val[1]
        return None

    '''
    Removes an item from the hash table using its key.
    If the key is found, the item is removed from its bucket.
    '''
    def remove(self, key):
        index = hash(key) % len(self.table)
        index_list = self.table[index]
        for key_val in index_list:
            if key_val[0] == key:
                index_list.remove([key_val[0], key_val[1]])
                return
