def loop_size(node):
    slow = node;
    fast = node;
    
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            slow = node
            
            while fast != slow:
                slow = slow.next
                fast = fast.next
            
            counter = 1
            slow = slow.next
            
            while fast != slow:
                slow = slow.next
                counter += 1
                
            return counter
            
    return 0