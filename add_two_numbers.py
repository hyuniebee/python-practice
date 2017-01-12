# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""

		# Initialize current node to dummy head of the returning list.
		current = dummy = ListNode(0)

		# Initialize carry to 0.
		carry = 0

		p = l1
		q = l2
		
		#Loop through lists l1 and l2 until you reach both ends.
		while l1 or l2:
			total = carry
			if l1:
				#print "Printing l1: %s " % l1.val
				#print "Printing l1 total before: %s " % total
				total = l1.val + total
				#print "Printing l1 total after: %s " % total
				l1 = l1.next
			if l2:
				#print "Printing l2: %s " % l2.val
				#print "Printing l2 total before: %s " % total
				total = l2.val + total
				#print "Printing l2 total after: %s " % total
				l2 = l2.next
			#print "%%%%%%%%"

			# Update carry = sum / 10.
			carry = total / 10

			# Create a new node 
			# This new node is  the digit value of (sum mod 10) and
			# set it to current node's next
			current.next = ListNode(total % 10)
			#print "ListNode %s" % current.val
 			temp = (total % 10)
			#print "Total mod 10 : %s " % temp
			# ... Then advance current node to next.
			current = current.next
			#print "ListNode AFTER %s" % current.val
			#print "$$$$$$$$$$$"

		# Check if carry = 1, if so append a new node with 
		# digit 1 to the returning list.
		if carry == 1:
			current.next = ListNode(1)
			#print "ListNode AFTER %s" % current.val
			#print "$$$$$$$$$$$"
		#print "Dummy.next %s" % dummy.next.val
		return dummy.next

test1, test1.next, test1.next.next = ListNode(2), ListNode(4), ListNode(3)
test2, test2.next, test2.next.next, test2.next.next.next = ListNode(5), ListNode(6), ListNode(5), ListNode(1)
output_ll = Solution().addTwoNumbers(test1, test2)
print "{0} -> {1} -> {2} -> {3}".format(output_ll.val, output_ll.next.val, output_ll.next.next.val, output_ll.next.next.next.val)