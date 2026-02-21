from contracts import Maze

class AdjacencyListMaze(Maze):
    def __init__(self,length,width):
        self.length = length
        self.width = width
        self.adjacency_list = {}

        for i in range(self.length*self.width):
            self.adjacency_list[i] = [] 

    def get_adj_list_idx(self, n):
        return n[1] + n[0]*self.width
    
    def get_node_coordinate(self, v):
        return (v // self.width, v % self.width)

    def add_edge(self, n1 : tuple, n2 : tuple):

        n1_idx = self.get_adj_list_idx(n1)
        n2_idx = self.get_adj_list_idx(n2)

        self.adjacency_list[n1_idx].append(n2_idx)

    def remove_edge(self, n1 : tuple, n2 : tuple):
        self.adjacency_list[n1].remove(n2)

    def has_edge(self,n1, n2) -> bool:
        return n2 in self.adjacency_list[n1]
    
    def get_edges(self,n:tuple) -> list:
        edges = []
        for v in self.adjacency_list[self.get_adj_list_idx(n)]:
            v_2d = self.get_node_coordinate(v)
            edges.append([n,v_2d])

        return edges
    
    def print_adjacency_list(self):
        for vertex, neighbors in self.adjacency_list.items():
            print(f"{vertex} -> {' '.join(map(str, neighbors))}")

    def print_maze(self):
        maze_string = ""

        hor_border_str = "-" * (self.width+2) + "\n"

        maze_string += hor_border_str

        for i in range(self.length):
            maze_string += "|"

            # Add vertical walls
            for j in range(self.width):
                maze_string += " "

                if not self.has_edge(i,j):
                    maze_string += "|"
                else:
                    maze_string += " "

            maze_string += "|\n"

            # Add horizontal walls
            for j in range(self.width):
                if not self.has_edge(i,j):
                    maze_string += "-"
                else:
                    maze_string += " "

            maze_string += " " * self.width
            maze_string += "|\n"

        maze_string += hor_border_str
        print(maze_string)