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
        distances = {node: float("inf") for node in self.adj_list}
        distances[start_node] = 0

        priority_queue = [(0, start_node)]
        visited = set()

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_node in visited:
                continue
            visited.add(current_node)

            for neighbour in self.obtain_neighbours(current_node):
                if isinstance(neighbour, tuple):
                    neighbour_node, weight = neighbour
                    weight = float(weight)
                else:
                    neighbour_node = neighbour
                    weight = 1

                distance = current_distance + weight

                if distance < distances[neighbour_node]:
                    distances[neighbour_node] = distance
                    heapq.heappush(priority_queue, (distance, neighbour_node))

        return distances

    def shortest_path(self, start_node, end_node):
        distances = {node: float("inf") for node in self.adj_list}
        previous_nodes = {node: None for node in self.adj_list}
        distances[start_node] = 0

        priority_queue = [(0, start_node)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_node == end_node:
                break

            for neighbour in self.obtain_neighbours(current_node):
                if isinstance(neighbour, tuple):
                    neighbour_node, weight = neighbour
                    weight = float(weight)
                else:
                    neighbour_node = neighbour
                    weight = 1

                distance = current_distance + weight

                if distance < distances[neighbour_node]:
                    distances[neighbour_node] = distance
                    previous_nodes[neighbour_node] = current_node
                    heapq.heappush(priority_queue, (distance, neighbour_node))


            path = []
            current = end_node
            while current is not None:
                path.insert(0, current)
                current = previous_nodes[current]

            if distances[end_node] == float("inf"):
                return None

            return path, distances[end_node]

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

    print("\nDIJKSTRA DISTANCES FROM A:")
    print(graph_obj.dijkstra("A"))

    print("\nSHORTEST PATH FROM A TO C:")
    path, distance = graph_obj.shortest_path("A", "C")
    print("Path:", path)
    print("Distance:", distance)








