class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Iteratively Space:O(1), Time: O(n)
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            nx = curr.next
            curr.next = prev
            prev = curr
            curr = nx
        return prev
     
     # Recursively Space:O(n), Time:O(n)
     def reverseList2(self, head):
        if not head or not head.next:
            return head

        reversed_head = self.reverseList2(head.next)

        head.next.next = head
        head.next = None

        return reversed_head





