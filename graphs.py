import heapq


class Graphs:
    def __init__(self, directed = False):
        self.directed = directed

        """
        graph = {
        A: (B, 2), (C, 27), (D, 89)
        }
        """
        self.adj_list = dict()  #holds key value pairs


    def __repr__(self):
        graph_string = ""


        for node, neighbours in self.adj_list.items():
            graph_string += f"{node} -> {neighbours}\n"

        return graph_string

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError("Node already exists")

    def add_edge(self, from_node, to_node, weight = None):
        if from_node not in self.adj_list:
            self.add_node(from_node)
        if to_node not in self.adj_list:
            self.add_node(to_node)

        if weight is None:
            self.adj_list[from_node].add(to_node)

            if not self.directed:
                self.adj_list[to_node].add(from_node)

        else:
            self.adj_list[from_node].add((to_node, weight))

            if not self.directed:
                self.adj_list[to_node].add((from_node, weight))

    def bfs(self, start_node):
        visited = set()
        queue = [start_node]
        order = []

        while queue:
            node = queue.pop(0)

            if node not in visited:
                visited.add(node)
                order.append(node)

                neighbours = self.obtain_neighbours(node)

                for neighbour in neighbours:
                    if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]
                    if neighbour not in visited:
                        queue.append(neighbour)

        return order

    def dfs(self, start_node):
        visited = set()
        stack = [start_node]
        order = []

        while stack:
            node = stack.pop()

            if node not in visited:
                visited.add(node)
                order.append(node)

                neighbours = self.obtain_neighbours(node)

                for neighbour in sorted(neighbours, reverse=True):
                    if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]
                    if neighbour not in visited:
                        stack.append(neighbour)

        return order



    def obtain_neighbours(self, node):
        return self.adj_list.get(node, set())

    def dijkstra(self, start_node):
        distances = {node: float("infinity") for node in self.adj_list}
        distances[start_node] = 0
        predecessors = {node: None for node in self.adj_list}
        priority_queue = [(0, start_node)] # (distance, node)

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbour_info in self.obtain_neighbours(current_node):
                if isinstance(neighbour_info, tuple):
                    neighbour, weight = neighbour_info
                else:
                    neighbour = neighbour_info
                    weight = 1

                distance = current_distance + weight

                if distance < distances[neighbour]:
                    distances[neighbour] = distance
                    predecessors[neighbour] = current_node
                    heapq.heappush(priority_queue, (distance, neighbour))

        return distances, predecessors

    def shortest_path_first(self, start_node, end_node):

        distances, predecessors = self.dijkstra(start_node)

        path = []
        current = end_node

        while current is not None and current in predecessors:
            path.append(current)
            current = predecessors[current]
            if current == start_node:
                path.append(current)
                break

            if current is None and end_node != start_node:
                return None

        if not path or path[-1] != start_node:
            return None

        return path[::1]

if __name__ == '__main__':
    graph_obj = Graphs(directed=True)

    graph_obj.add_edge("A", "B", 2)
    graph_obj.add_edge("A", "J", 2)
    graph_obj.add_edge("A", "C", 3)
    graph_obj.add_edge("A", "D", 4)
    graph_obj.add_edge("B", "D", 4)
    graph_obj.add_edge("D", "C", 7)


    print(graph_obj)
    print("BREADTH FIRST SEARCH: \n")
    print(graph_obj.bfs("A"))
    print("DEPTH FIRST SEARCH: ")
    print(graph_obj.dfs("A"))
    print("\nDIJKSTRA'S ALGORITHM: ")
    distances, predecessors = graph_obj.dijkstra("A")
    print("Distances:", distances)
    print("Predecessors:", predecessors)

    print("\nSHORTEST PATH FIRST (A to C):")
    path_a_c = graph_obj.shortest_path_first("A", "C")
    print(f"Path from A to C: {path_a_c}")

    print("\nSHORTEST PATH FIRST (A to J):")
    path_a_j = graph_obj.shortest_path_first("A", "J")
    print(f"Path from A to J: {path_a_j}")








