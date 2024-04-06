class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    prev_elem = None
    new_linked_list = None
    while head:
        new_linked_list = Node(head.data)
        new_linked_list.next = prev_elem
        prev_elem = new_linked_list
        head = head.next
    return new_linked_list