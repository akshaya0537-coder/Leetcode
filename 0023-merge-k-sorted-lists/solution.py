# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        n=len(lists)
        l1=lists[0]
        
        for i in range(1,n):
            ans=ListNode()
            ptr=ans
            l2=lists[i]
            
            while l1 and l2:
                if l1.val<=l2.val:
                    ptr.next=l1
                    l1=l1.next
                    ptr=ptr.next
                else:
                    ptr.next=l2
                    l2=l2.next
                    ptr=ptr.next
            if l1:
                ptr.next=l1
            if l2:
                ptr.next=l2

            ptr=ans.next
            l1=ans.next

        return l1
        
