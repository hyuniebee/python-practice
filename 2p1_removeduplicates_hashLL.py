class Node(object):
	def __init__(self):
		self.data = None
		self.next = None
	def get_data(self):
		return self.data
	def get_next_data(self):
		return self.data.next

class LinkedList (object):
	def __init__(self):
		self.head = None

	def insert(self, data):
		new_node = Node()
		new_node.data = data
		new_node.next = self.head
		self.head = new_node

	def display(self):
		current_node = self.head
		while current_node:
			print current_node.data
			current_node = current_node.next

	def get_size(self):
		current_node = self.head
		count = 0
		while(current_node):
			count += 1
			current_node = current_node.next
		return count


class Solution (object):
	def remove_duplicates(self, ll):
		input_current_node = ll.head
		my_ll = LinkedList()
		my_dict = {}
		count = 0
		while (input_current_node):
			current_data = input_current_node.get_data()
			if current_data not in my_dict:
				my_ll.insert(current_data)
			my_dict[current_data] = []
			my_dict[current_data].append(count)
			input_current_node = input_current_node.next
			count += 1
		my_ll.display()

ll = LinkedList()
ll.insert('f')
ll.insert('o')
ll.insert('l')
ll.insert('l')
ll.insert('o')
ll.insert('w')
ll.insert('u')
ll.insert('p')
Solution().remove_duplicates(ll)
