def swap_pairs(head):
    if head == None:
        return None
    counter = 0
    first = None
    second = None
    linked_list = []
    while head:
        if counter % 2 == 0:
            first = head
            if head.next == None:
                linked_list.append(first)
        if counter % 2 == 1:
            second = head
            linked_list.extend([second, first])
        head = head.next  
        counter += 1
        
    next = None
    for node in linked_list[::-1]:
        node.next = next
        next = node
    
    return linked_list[0]