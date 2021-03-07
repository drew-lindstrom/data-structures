from linked_list import LinkedList


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.array = []
        for i in range(vertices):
            temp = LinkedList()
            self.array.append(temp)

    def add_edge(self, source, destination):
        if source < self.vertices and destination < self.vertices:
            # Directed Implementation
            self.array[source].insert_at_head(destination)

            # Undirected Implementation
            # self.array[destination].insert_at_head(source)

    def print_graph(self):
        print(">> Adjacency List of Directed Graph <<")
        print()
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            temp = self.array[i].get_head()
            while temp is not None:
                print("[", temp.data, end=" ] -> ")
                temp = temp.next
            print("None")


def transpose(my_graph):
    new_graph = Graph(my_graph.V)

    for source in range(my_graph.V):

        while my_graph.graph[source] is not None:

            destination = my_graph.graph[source].vertex
            new_graph.add_edge(destination, source)
            my_graph.graph[source] = my_graph.graph[source].next

    return new_graph


graph = Graph(8)
graph.add_edge(1, 4)
graph.add_edge(1, 5)
graph.add_edge(4, 6)
graph.print_graph()