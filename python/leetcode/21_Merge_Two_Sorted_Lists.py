# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 == None or list2 == None:
            return list1 or list2

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """


# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
list1 = [1,2,4]
list2 = [1,3,4]
print(Solution().mergeTwoLists(list1,list2))

# Example 2:
# Input: list1 = [], list2 = []
# Output: []
list1 = []
list2 = []
print(Solution().mergeTwoLists(list1,list2))

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]
list1 = []
list2 = [0]
print(Solution().mergeTwoLists(list1,list2))