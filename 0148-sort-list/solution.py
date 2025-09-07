# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Step 1: Divide the list
        mid = self.find_middle(head)
        right_half = mid.next
        mid.next = None  # Break the link to separate lists

        # Step 2: Recursively sort sub-lists
        left_sorted = self.sortList(head)
        right_sorted = self.sortList(right_half)

        # Step 3: Merge sorted sub-lists
        return self.merge_two_lists(left_sorted, right_sorted)

    def find_middle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        current.next = l1 or l2
        return dummy.next
