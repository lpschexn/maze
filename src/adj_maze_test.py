from mazes.adjacency_list_maze import AdjacencyListMaze

tmp = AdjacencyListMaze(5,5)
tmp.add_edge((0,0),(0,1))
tmp.print_adjacency_list()
print(tmp.get_edges((0,0)))