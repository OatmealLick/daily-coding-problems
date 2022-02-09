from collections import defaultdict


class GraphColorer:
    """
    Given an undirected graph represented as an adjacency matrix and an integer k,
    write a function to determine whether each vertex in the graph can be colored such that
    no two adjacent vertices share the same color using at most k colors.
    """

    def can_be_colored_2(self,
                         adjacency_matrix: list[list[int]],
                         max_colors: int):
        """
        Second, enhanced approach.
        Solution using backtracking and proper (given) graph representation.
        """
        return self._do_can_be_colored_2(0, {}, adjacency_matrix, max_colors)

    def _do_can_be_colored_2(self,
                             node: int,
                             colors: dict[int, int],
                             adjacency_matrix: list[list[int]],
                             max_colors: int):
        if node == len(adjacency_matrix):
            return True

        for color in range(max_colors):
            colors[node] = color
            if self._is_valid(node, colors, adjacency_matrix):
                if self._do_can_be_colored_2(node + 1, colors, adjacency_matrix, max_colors):
                    return True
            colors.pop(node)
        return False

    def _is_valid(self,
                  node: int,
                  colors: dict[int, int],
                  adjacency_matrix: list[list[int]]) -> bool:
        colored = [n for n in self._neighbors(node, adjacency_matrix) if n in colors]
        return all([colors[n] != colors[node] for n in colored])

    def _neighbors(self, node: int, adjacency_matrix: list[list[int]]) -> list[int]:
        return [n for n in range(len(adjacency_matrix[node])) if adjacency_matrix[node][n] == 1]

    def can_be_colored_1(self,
                         neighbors: dict[int, list[int]],
                         max_colors: int,
                         start: int = 1) -> bool:
        """
        First naive approach.
        It was BFS search with proper coloring of nodes.
        It accepts graph as list of connections to neighbors
        """
        assert max_colors > 0
        assert start in neighbors
        nodes = [start]
        back_neighbors = defaultdict(lambda: [])
        visited = set()
        colors = {}
        while nodes:
            node = nodes.pop(0)
            if node not in visited:
                visited_neighbors = [n for n in neighbors[node] if n in visited]
                node_back_neighbors = [n for n in back_neighbors[node] if n in visited and n not in visited_neighbors]
                visited_neighbors += node_back_neighbors
                color = self._find_color(visited_neighbors, colors, max_colors)
                if color == -1:
                    return False
                colors[node] = color
                for n in neighbors[node]:
                    if node not in back_neighbors[n]:
                        back_neighbors[n].append(node)
                    if n not in visited:
                        nodes.append(n)
                visited.add(node)
        return True

    def _find_color(self, neighbors: list[int], colors: dict[int, int], max_colors: int):
        color_occurrences = defaultdict(int)
        for neighbor in neighbors:
            color_occurrences[colors[neighbor]] += 1

        for color in range(max_colors):
            if color_occurrences[color] == 0:
                return color
        return -1
