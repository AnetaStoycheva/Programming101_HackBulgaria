import unittest
from follow_github import DirectedGraph


class TestDirectedGraph(unittest.TestCase):
    def setUp(self):
        self.node_a = 'node_a'
        self.node_b = 'node_b'
        self.node_c = 'node_c'
        self.graph1 = DirectedGraph()

    def test_add_edge(self):
        self.graph1.add_edge(self.node_a, self.node_b)
        self.assertEqual(self.graph1.get_neighbours_for(self.node_a), [self.node_b])
        self.graph1.add_edge(self.node_c, self.node_a)
        self.assertEqual(self.graph1.get_neighbours_for(self.node_a), [self.node_b])

    def test_path_between_connected_nodes(self):
        self.graph1.add_edge(self.node_a, self.node_b)
        self.graph1.add_edge(self.node_b, self.node_c)
        self.assertTrue(self.graph1.path_between(self.node_a, self.node_b))
        self.assertTrue(self.graph1.path_between(self.node_a, self.node_c))

    def test_no_path_between_nodes(self):
        self.graph1.add_edge(self.node_a, self.node_b)
        self.graph1.add_edge(self.node_b, self.node_c)
        self.assertFalse(self.graph1.path_between(self.node_b, self.node_a))
        self.assertFalse(self.graph1.path_between(self.node_c, self.node_a))


if __name__ == '__main__':
    unittest.main()
