# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            # 1. Get the digits from both of them
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # 2. For new digit
            val = v1 + v2 + carry
            # 3. For vals like 15
            carry = val // 10
            val = val % 10
            # 4. Add it to the List
            cur.next = ListNode(val)
            # 5. Update cur
            cur = cur.next
            # 6. Check if ln is not Null
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        # 7. Return value
        return dummy.next

