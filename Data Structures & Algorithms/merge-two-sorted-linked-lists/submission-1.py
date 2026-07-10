# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

####already sorted!
## compare heads of both lists, figure which is smaller and thats head of newlist
## then make other head next, then compare nex

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode() ## initialize how?...
        curr = list1
        tail = res

        while list1 and list2:
            
            if list1.val <= list2.val:
                curr = list1
            else:
                curr = list2
            tail.next = curr ## so first number
            tail = tail.next
            ##res.next.next = prev
            if curr == list1:
                list1 = list1.next
            else:
                list2 = list2.next
            ##prev = list2.next
        if list1 == None:
            curr = list2
            tail.next = curr
        else:
            curr = list1
            tail.next = curr

        return res.next

                #...reassign next of head to be the max of list[0] and list[0]
                #...