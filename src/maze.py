class Maze:
    def __init__(self,length,width):
        self.length = length
        self.width = width
        self.adj_matrix = []

        # Adjacency Matrix
        for i in range(0,self.length):
            row = []
            for j in range(0,self.width):
                row.append(0)
            self.adj_matrix.append(row)

    def add_edge(self, n1 : int,n2 : int) -> None:
        # Undirected
        self.adj_matrix[n1][n2] = 1
        self.adj_matrix[n2][n1] = 1

    def print_adjacency_matrix(self) -> None:
        for row in self.adj_matrix:
            print(" ".join(map(str,row)))