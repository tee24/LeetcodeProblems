class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head):
        if not head:
            return None
        def helper(head):
            curr = head
            while curr:

                if curr.child:
                    temp_next = curr.next
                    curr.next = curr.child
                    curr.child.prev = curr
                    temp = curr.child
                    curr.child = None
                    curr = helper(temp)
                    if temp_next:
                        curr.next = temp_next
                        temp_next.prev = curr
                if curr.next:
                    curr = curr.next
                else:
                    break
            return curr
        head = helper(head)

        while head.prev:
            head = head.prev
        return head


# Space, Time =  O(1), O(n) where n is the number of nodes in the unflattened list.


def flatten(head):
    if not head:
        return None

    s, nodes = [head], [] # use stack to perform dfs on structure.

    while s: # while stack is not empty.

        node = s.pop()
        nodes.append(node)

        if node.next:
            s.append(node.next)
        if node.child:
            s.append(node.child)
        

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i+1]
        nodes[i+1].prev = nodes[i]
        nodes[i].child = None

    return nodes[0]

# Space, Time = O(n) (Storing nodes in nodes array), O(n)







