class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from queue import deque
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return None
        
        q = deque()
        temp = head
        q.append(temp)
        
        while temp.next:
            q.append(temp.next)
            temp = temp.next
        
        curr = head
        q.popleft()
        i = 0
        
        while len(q) > 0:
            if i%2 == 0:
                new = q.pop()
            else:
                new = q.popleft()
            temp = curr.next
            curr.next = new
            curr = new
            i+=1
        curr.next = None
        

# Space, Time: O(n)