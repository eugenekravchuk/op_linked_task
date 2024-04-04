from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
    
def push(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def build_one_two_three():
    one = push(None, 3)
    second = push(one, 2)
    third = push(second, 1)
    return third