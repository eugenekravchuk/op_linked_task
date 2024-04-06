def linked_list_from_string(s):
    if s == "None":
        return None
    raw_list = s.split(" -> ")[0:-1]
    linked_list = Node(int(raw_list[-1]))
    for node in raw_list[::-1][1:]:
        linked_list = Node(int(node), linked_list)
    return linked_list