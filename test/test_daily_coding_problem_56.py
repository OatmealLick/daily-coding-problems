from problems.daily_coding_problem_56 import GraphColorer

colorer = GraphColorer()


def test_simple_graph_that_can_be_colored():
    assert colorer.can_be_colored_1(diamond_graph_neighbors(), max_colors=2)


def test_complex_graph_that_can_be_colored():
    assert colorer.can_be_colored_1(complex_graph_neighbors(), max_colors=3)


def test_simple_graph_that_cannot_be_colored():
    assert not colorer.can_be_colored_1(diamond_graph_neighbors(), max_colors=1)


def test_complex_graph_that_cannot_be_colored():
    assert not colorer.can_be_colored_1(complex_graph_neighbors(), max_colors=2)


def test_simple_graph_that_can_be_colored_2():
    assert colorer.can_be_colored_2(diamond_graph_adjacency_matrix(), max_colors=2)


def test_complex_graph_that_can_be_colored_2():
    assert colorer.can_be_colored_2(complex_graph_adjacency_matrix(), max_colors=3)


def test_simple_graph_that_cannot_be_colored_2():
    assert not colorer.can_be_colored_2(diamond_graph_adjacency_matrix(), max_colors=1)


def test_complex_graph_that_cannot_be_colored_2():
    assert not colorer.can_be_colored_2(complex_graph_adjacency_matrix(), max_colors=2)


def diamond_graph_neighbors():
    return {1: [2, 3], 2: [4], 3: [4], 4: []}


def diamond_graph_adjacency_matrix():
    return [
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [0, 1, 1, 0],
    ]


def complex_graph_adjacency_matrix():
    return [
        [0, 1, 0, 1, 0, 0, 1, 1],
        [1, 0, 1, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 1, 0],
        [1, 0, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0]
    ]


def complex_graph_neighbors():
    return {
        1: [2, 4, 7],
        2: [3, 4],
        3: [4],
        4: [5, 6, 7],
        5: [7],
        6: [7],
        7: [8],
        8: [1]
    }
