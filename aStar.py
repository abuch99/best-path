class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position=position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.f))

def aStar(graph,nodedict, durations,start,end):
    start_node = Node(None,start)
    end_node = Node(None,end)
    
    open_list=[]
    closed_list=[]
    graph_dict=graph.getGraph()

    # for key, value in graph_dict.items():
    #     print (key + ' | ' + str(graph_dict[key]))
    #     print('-----------')
    open_list.append(start_node)
    count=0
    while(len(open_list)>0):

        open_list.sort()
        current_node = open_list.pop(0)
        closed_list.append(current_node)
        # If RGIA is found
        print(current_node)
        if current_node.position == end_node.position:
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
            if child in closed_list:
                continue

            source=current_node.position
            dest=child.position

            if child in open_list:
                new_g = current_node.g + durations[(source,dest)] 
                if child.g < new_g:
                    child.g = new_g
                    child.parent=current_node
            
            else: 
                child.g = child.g + durations[(source,dest)]
                child.h = durations[(dest,end)]
                child.f = child.g + child.h
                child.parent=current_node
                open_list.append(child)
        count+=1
            # print(source,dest)
            # print(child.f)
            # print('----------')
    raise ValueError('No Path Found')
    return []