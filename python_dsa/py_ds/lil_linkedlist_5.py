# Doubly Linked List Class - LinkedIn Learning


'''Node Class'''

class DLLNode: #Doubly Linked List (DLL)
	
	def __init__(self, data):
		self.data = data
		self.next = None
		self.previous = None
		
	def __repr__(self):
		return 'DLLNode object: data={}'.format(self.data)
		
	def get_data(self):
		'''Return the self.data attribute'''
		return self.data
		
	def set_data(self, new_data):
		'''Replace the existing value of the self.data attribute with new_data parameter'''
		self.data = new_data
		
	def get_next(self):
		'''Return the self.next attribute'''
		return self.next
		
	def set_next(self, new_next):
		'''Replace the existing value of the self.next attribute with new_next parameter.'''
		self.next = new_next
		
	def get_previous(self):
		'''Return the self.previous attribute'''
		return self.previous
	
	def set_previous(self, new_previous):
		'''Replace the existing value of the self.previous attribute with new_previous parameter.'''
		self.previous = new_previous
		
'''Doubly Linked List Class'''

class DLL:
	
	def __init__(self):
		self.head = None
		
	def __repr__(self):
		return '<DLL object: head=>'.format(self.head)
		
	def is_empty(self):
		return self.head is None
		
	def size(self):
		'''Traverse the linked list and returns an int value representing the number of nodes in the list. Time Complexity: O(n) bc every node in the linked list must be visited in order to calculate the total size'''
		size = 0
		if self.head is None:
			return 0
		
		current = self.head
		
		while current is not None: #While there are still nodes present
			size += 1
			current = current.get_next()
			
		return size
		
	def search(self, data):
		'''Traverses the linked list and returns True if the data searched for is present in one of the Nodes. Otherwise, it returns False.
		
		Time Complexity is O(n) bc every node must be visited in the worst case scenario.'''
		if self.head == None:
			return 'Linked list is empty. No nodes to search.'
		
		current = self.head
		while current is not None:
			# The Node's data matches what we're looking for
			if current.get_data() == data:
				return True
			# The Node's data doesn't match
			else:
				current = current.get_next()
				
		return False
		
	def add_front(self, new_data):
		'''Add a Node whose data is the new_data argument to the front of the linked list''' 
		temp = DLLNode(new_data)
		temp.set_next(self.head)
		
		if self.head is not None:
			self.head.set_previous(temp)
			
		self.head = temp
		
		
	def remove(self, data):
		'''Removes the first occurence of a Node that contains the data argument as its self.data attribute. Returns nothing.
		
		The time complexity is O(n) bc in the worst case scenario, we have to visit every node before finding the one we want to remove.
		'''
		if self.head is None:
			return 'Linked list is empty. No nodes to remove.'
		
		current = self.head
		found = False
		while not found:
			if current.get_data() == data:
				found = True
			else:
				if current.get_next() is None:
					return 'A Node with that data value is not present.'
				else:
					current = current.get_next()
		
		if current.previous is None:
			self.head = current.get_next() #get the second node
		else:
			current.previous.set_next(current.get_next())
			current.next.set_previous(current.get_previous())
		
	'''Test cases'''
dll = DLL()
print(dll.size)
dll.add_front(1)
print(dll.head)
print(dll.size)
print(dll.head.previous)
print(dll.head.next)
dll.add_front(2)
print(dll.head)
print(dll.size)
print(dll.head.previous)
print(dll.head.next)
print(dll.head.next.next)
