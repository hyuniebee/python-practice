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

		# Initialize linked lists
		current = return_list = ListNode(0)

		# Init carry to 0
		carry = 0

		# Go through both linked lists, l1 and l2
		while l1 or l2:
			total = carry # Because if a carry value has occured, need to add 1 to total sum of that column
			if l1: # Go through l1 as long as it's not NULL
				total = l1.val + total
				l1 = l1.next
			if l2: #Same as l1 onto l2
				total = l2.val + total
				l2 = l2.next
			carry = total / 10 # This is to determine if the value was less than 10 (no carry) or greater than 10 (carry)
			current.next = ListNode(total % 10) #( Total in that column is the mod of the total)
			current = current.next

		# Compensate for extra carry at end (example 99 + 1 = 100)
		if carry == 1:
			current.next = ListNode(1)
			current = current.next

		return return_list.next


test1 = ListNode(1)
test2, test2.next = ListNode(9), ListNode(9)
return_list = Solution().addTwoNumbers(test1, test2)
print "{0} -> {1} -> {2}".format(return_list.val, return_list.next.val, return_list.next.next.val)