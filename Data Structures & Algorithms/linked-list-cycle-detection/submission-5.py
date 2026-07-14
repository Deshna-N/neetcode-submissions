# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        
        while fast and fast.next: ## while its not an empty node
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
                









        
        ## initliaze and add onto number count
           # if head.val not in mydict: 
            #    mydict[head.val] = 0
         #   mydict[head.val] += 1
        ## check if 2 or more exists, because thats a cycle
          #  if mydict[head.val] >= 2: ## there's a cycle :O
           #     return True

        ## iterating forward in Linked List
          #  prev = head
         #   head = head.next
        ## finished linked list and no cycle detected
       # return False

            
            

         