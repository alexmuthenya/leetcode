# A class that represents a single node in a linked list.
# Each node stores a value and a reference to the next node.
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value   # The digit stored in this node
        self.next = next     # Pointer to the next node in the list


class Solution:
    def addTwoNumbers(self, l1, l2):
        # Create a dummy node to make building the result list easier.
        # We will return dummy.next at the end.
        dummy = ListNode(0)

        # 'current' will point to the last node in the result list as we build it.
        current = dummy

        # This will store any carry we get when digits add up to >= 10.
        carry = 0


        # Loop as long as there is something to process:
        # - l1 still has nodes
        # - l2 still has nodes
        # - or we still have a carry to add
        while l1 or l2 or carry:

            # Get the value from the l1 node if it exists, otherwise use 0
            x = l1.value if l1 else 0

            # Get the value from the l2 node if it exists, otherwise use 0
            y = l2.value if l2 else 0   # FIXED: You previously wrote "if l1" here by mistake


            # Add the two digits plus any leftover carry
            total = x + y + carry

            # New carry will be the tens place of the total (e.g. 15 -> carry = 1)
            carry = total // 10

            # The digit to store in the new node is the ones place (e.g. 15 -> digit = 5)
            digit = total % 10


            # Create a new node with this digit and attach it to the result list
            current.next = ListNode(digit)

            # Move 'current' forward to this new node
            current = current.next


            # Move to the next node in l1 if it exists
            if l1:
                l1 = l1.next

            # Move to the next node in l2 if it exists
            if l2:
                l2 = l2.next


        # Return the first real node of the result list (skipping the dummy node)
        return dummy.next
