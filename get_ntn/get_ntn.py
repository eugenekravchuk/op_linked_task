from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    if node == None:
        raise Exception("Sorry, no such Node")
    if index < 0:
        raise Exception("Sorry, no index below zero")
    current_node = node
    for i in range(index):
        current_node = current_node.next
        if current_node == None:
             raise Exception("Sorry, no index below zero")
    return current_node