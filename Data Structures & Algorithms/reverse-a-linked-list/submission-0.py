# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

 ## [0      1       2       3     null]
 ## [



class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # pointers
        prev = None ## the head of my reversed list
        curr = head
        n = head
        
        ## base case
        if curr == None:
            return None

        while curr: ## first iteration curr is 0 [0 1 2 3 null]
            n = curr.next # n has 1, 2, 3, null
            curr.next = prev # makes [0 -> None] ## for reversing 
            prev = curr # prev is now 0 -> None
            curr = n  # curr is 1, 2, 3, 0, None
        return prev


            #n = 2, 3, None
            # curr.next(1) is 0->None
            # prev = 1 -> 0 -> None
            # curr = 2 -> 3

            # n = 3 -> None
            # curr.next(2) is 1 -> 0 -> None
            # prev = 2 -> 1 -> 0 -> None
            # curr = 3 -> None

            # n = None
            # curr.next (3) -> 2->1->0
            # prev = 3 -> 2 -> 1 -> 0 -> None
            # curr = None
            


            



            







        