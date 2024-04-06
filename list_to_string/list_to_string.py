def stringify(node):
    if node == None:
        return "None"
    current_node = node
    string_represent = f"{current_node.data} -> "
    while current_node.next != None:
        current_node = current_node.next
        string_represent += f"{current_node.data} -> "
    else:
        string_represent += "None"
        
    return string_represent
        