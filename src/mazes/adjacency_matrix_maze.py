from contracts import Maze

class AdjacencyMatrixMaze(Maze):
    def __init__(self,length,width):
        self.length = length
        self.width = width
        self.adj_matrix = []

        # Adjacency Matrix
        for i in range(0,self.length):
            row = []
            for j in range(0,self.width):
                row.append(False)
            self.adj_matrix.append(row)

    def add_edge(self, n1 : int, n2 : int):
        # Undirected
        self.adj_matrix[n1][n2] = True
        self.adj_matrix[n2][n1] = True

    def remove_edge(self, n1 : int, n2 : int):
        # Undirected
        self.adj_matrix[n1][n2] = False
        self.adj_matrix[n2][n1] = False

    def has_edge(self,n1 : int, n2 : int) -> bool:
        return self.adj_matrix[n1][n2]

    def print_adjacency_matrix(self) -> None:
        for row in self.adj_matrix:
            print(" ".join(map(str,row)))