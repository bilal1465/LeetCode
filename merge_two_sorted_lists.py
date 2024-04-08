class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):

    merged = ListNode()

    current = merged

    p1, p2 = list1, list2

    while p1 and p2:
        if p1.val < p2.val:
            current.next = p1
            p1 = p1.next
        else:
            current.next = p2
            p2 = p2.next
        current = current.next

    current.next = p1 if p1 else p2
    
    return merged.next

list1 = ListNode(2)
list1.next = ListNode(5)
list1.next.next = ListNode(7)

list2 = ListNode(6)
list2.next = ListNode(7)
list2.next.next = ListNode(8)

# Merge the two lists
merged_list = mergeTwoLists(list1, list2)

# Print the merged list for demonstration
while merged_list:
    print(merged_list.val, end=" -> ")
    merged_list = merged_list.next
    



