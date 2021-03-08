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


def DFS(my_graph, source):
    visited = [False] * (len(my_graph.graph))
    stack = []
    result = ""

    stack.append(source)

    while stack:
        source = stack.pop()

        if not visited[source]:
            result += str(source)
            visited[source] = True

        while my_graph.graph[source] is not None:
            data = my_graph.graph[source].vertex
            if not visited[data]:
                stack.append(data)
            my_graph.graph[source] = my_graph.graph[source].next


def transpose(my_graph):
    new_graph = Graph(my_graph.V)

    for source in range(my_graph.V):

        while my_graph.graph[source] is not None:

            destination = my_graph.graph[source].vertex
            new_graph.add_edge(destination, source)
            my_graph.graph[source] = my_graph.graph[source].next

    return new_graph


def find_all_paths_recursive(graph, source, destination, visited, path, paths):
    visited[source] = True
    path.append(source)

    if source == destination:
        paths.append((path))
    else:
        while graph.graph[source] is not None:
            i = graph.graph[source].vertex

            if not visited[i]:
                find_all_paths_recursive(graph, i, destination, visited, path, paths)

            graph.graph[source] = graph.graph[source].next

    path.pop()
    visited[source] = False


def find_all_paths(graph, source, destination):
    visited = [False] * (graph.V)

    paths = []
    path = []

    find_all_paths_recursive(graph, source, destination, visited, path, paths)
    return paths


def remove_edge(graph, source, destination):

    if graph.V == 0:
        return graph

    if source >= graph.V or source < 0:
        return graph

    if destination >= graph.V or destination < 0:
        return graph

    temp = graph.graph[source]

    if temp is not None:
        if temp.vertex == destination:
            graph.graph[source] = temp.next
            temp = None
            return

    while temp is not None:
        if destination == temp.vertex:
            break
        prev = temp
        temp = temp.next

    if temp is None:
        return

    prev.next = temp.next
    temp = None


def detect_cycle(graph):
    visited = [False] * graph.V

    my_stack = [False] * graph.V

    for node in range(graph.V):
        if detect_cycle_recursive(graph, node, visited, my_stack):
            return True

    return False


def detect_cycle_recursive(graph, node, visited, my_stack):
    if my_stack[node]:
        return True

    if visited[node]:
        return False
    visited[node] = True
    my_stack[node] = True

    head = graph.graph[node]
    while head is not None:
        adjacent = head.vertex
        if detect_cycle_recursive(graph, adjacent, visited, my_stack):
            return True
        head = head.next

    my_stack[node] = False
    return False


graph = Graph(8)
graph.add_edge(1, 4)
graph.add_edge(1, 5)
graph.add_edge(4, 6)
graph.print_graph()