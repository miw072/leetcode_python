class LRUCache:

	class Node:
		def __init__(self, key, value):
			self.prev = None
			self.key = key
			self.value = value
			self.next = None

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity, self.dict = capacity, {}
        self.head, self.tail = self.Node('head', 'head'), self.Node('tail', 'tail')
        self.head.next = self.tail
        self.tail.prev = self.head

    # @return an integer
    def get(self, key):
		if key not in self.dict:
			return -1
		else:
			self.insertAfterFirst(self.unlinknode(self.dict[key]))
			return self.dict[key].value	        

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
    	if key in self.dict:
    		self.insertNodeAtFirst(self.unlinkNode(self.dict[key]))
    		self.dict[key].value = value
    	else:
    		if len(self.dict > self.capacity):
    			del self.dict[self.unlinkNode(self.tail.prev).key]
    		self.dict[key] = self.Node(key, value)
    		self.insertNodeAtFirst(self.dict[key])		

    def unlinknode(self, node):
    	node.prev.next = node.next
    	node.next.prev = node.prev
    	node.prev = None
    	node.next = None
    	return node

    def insertAfterFirst(self, node):
    	node.prev = self.head
    	node.next = self.head.next
    	self.head.next.prev = node
    	self.head.next = node	