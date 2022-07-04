


class Graph:
    def __init__(self, edges):
        self.edges = edges 
        self.graph_dict = {}

        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]



    def get_paths(self,start,end,path=[]):
         path = path+[start]
         
         # if both start and end are same
         if start==end:
            return [path]

         #if start location is not in the dict keys   
         if start not in self.graph_dict:
            return []

         paths = []

         #traberse the keys
         for node in self.graph_dict[start]:
            if node not in path:
                #find the path between node and end
                new_path = self.get_paths(node,end,path)
                for p in new_path:
                    paths.append(new_path)

         return paths


    def get_shortest_path(self,start,end,path=[]):
        path = path + [start]

        if start==end:
            return path
        
        if start not in self.graph_dict:
            return None

        shortest_path = None 

        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node,end,path)
                if sp:
                    if shortest_path is None or len(sp)<len(shortest_path):
                        shortest_path = sp 

        return shortest_path

            




if __name__ == "__main__":

    routes = [
        ("Mumbai","Paris"),
        ("Mumbai","Dubai"),
        ("Paris","Dubai"),
        ("Paris","New York"),
        ("Dubai","New York"),
        ("New York","Toronto")
    ]

    graph = Graph(routes)
    path = graph.get_shortest_path("Mumbai","New York")
    print(path)