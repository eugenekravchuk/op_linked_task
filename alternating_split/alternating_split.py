class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    first_list = []
    second_list = []
    counter = 0
    
    first_node = None
    second_node = None
    
    while head:
        if counter % 2 == 0:
            first_list.append(head)
        else:
            second_list.append(head)
        head = head.next
        counter += 1
        
    if not first_list or not second_list:
        raise Exception("Wrong")

    for node in first_list[::-1]:
        node.next = first_node
        first_node = node
    for node in second_list[::-1]:
        node.next = second_node
        second_node = node
        
    return Context(first_node, second_node)