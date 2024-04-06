""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    linked_list = [data]
    new_linked_list = None
    while head:
        linked_list.append(head.data)
        head = head.next
    for node in sorted(linked_list)[::-1]:
        formed_node = Node(node)
        formed_node.next = new_linked_list
        new_linked_list = formed_node
        
    return new_linked_list