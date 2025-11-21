# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # collect (we are mergering the enitire list nodes into a single array)
        arr = []
        for node in lists: # one head pointer at a time
            while node: # traverse that linked list fully
                arr.append(node.val)
                node = node.next
        
        # print(arr) # basically we flattened the array


        # sort O(N logN)
        arr.sort() # reorder the elements in place (TimSort)


        # rebuild as a Linked List
        dummy = ListNode()
        tail = dummy

        for val in arr:
            tail.next = ListNode(val)
            tail = tail.next

        return dummy.next

        # # T.C = O(N) + O(N log N) + O(N) (flatten+sort+rebuild)= O(N log N)
        # # S.C = O(N)


        # """
        # Start with an empty array arr = []
        # Loop through each list
        # For each list, walk through nodes one by one
        # Append each node’s value to the array
        # When done, sort arr
        # Build a new list using sorted values
        # """
