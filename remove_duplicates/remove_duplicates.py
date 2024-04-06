class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def remove_duplicates(head):
    
    linked_list = []
    nodes = None

    while head:
        linked_list.append(head.data)
        head = head.next
        
    linked_list = list(set(linked_list))

    for node in linked_list[::-1]:
        nodes = Node(node, nodes)
    
    return nodes