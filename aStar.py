class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position=position

        self.g = 0
        self.h = 0
        self.f = 0

def aStar(graph,nodedict, durations,start,end):
    start_node = Node(None,start)
    end_node = Node(None,end)
    
    open_list=[]
    closed_list=[]
    graph_dict=graph.getGraph()
    open_list.append(start_node)

    while(len(open_list)>0):
        current_node=open_list[0]
        current_index=0

        for index,item in enumerate(open_list):
            if item.f<current_node.f:
                current_node=item
                current_index=index
        
        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == end_node:
            print('entered')
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]
        
        children=[]
        temp=graph_dict[current_node.position]
        for item in temp:
            new_node = Node(current_node,item)
            children.append(new_node)

        for child in children:
            for closed_child in closed_list:
                if child == closed_child:
                    continue
            
            temp_parent=child.parent

    return []