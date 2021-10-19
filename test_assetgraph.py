import unittest
import assetgraph


class TestGraph(unittest.TestCase):


    def setUp(self):
        super(TestGraph, self).setUp()
        self.graph = assetgraph.Graph()

    # Test for add vertex function
    def test_addVertex(self):

        # Adding vertex on level 1
        graph = self.graph
        Inv1 = graph.addVertex('Inv1', 1)
        actual_output = graph.displayGraph()
        expected_output = {Inv1: []}
        self.assertEqual(actual_output, expected_output)

        # Adding vertex on level 2
        F1 = graph.addVertex('F1', 2)
        actual_output = graph.displayGraph()
        expected_output = {Inv1: [], F1: []}
        self.assertEqual(actual_output, expected_output)

        # Checking Exception
        self.assertRaises(ValueError, graph.addVertex, 'F1', 4)
        self.assertRaises(ValueError, graph.addVertex, 'F1', 0)
        self.assertRaises(ValueError, graph.addVertex, 'F1', -1)
        self.assertRaises(ValueError, graph.addVertex, 'H1', 3)

    # Test for adding Edges
    def test_addEdges(self):
        graph = self.graph
        # Adding Edge between Investor and Fund
        Inv1 = graph.addVertex('Inv1', 1)
        F1 = graph.addVertex('F1', 2)
        graph.addEdge((Inv1, F1))
        actual_output = graph.displayGraph()
        expected_output = {Inv1: [(F1, 0)], F1: []}
        self.assertEqual(actual_output, expected_output)

        # Adding another Edge between Fund and Holding
        H1 = graph.addVertex('H1', 3, 10)
        graph.addEdge((F1, H1), 100)
        actual_output = graph.displayGraph()
        expected_output = {Inv1: [(F1, 0)], F1: [(H1, 100)], H1: []}
        self.assertEqual(actual_output, expected_output)

    # Test Vertices Count
    def test_getVerticesCount(self):
        graph = self.graph
        Inv1 = graph.addVertex('Inv1', 1)
        F1 = graph.addVertex('F1', 2)
        actual_output = graph.getVerticesCount()
        expected_output = 2
        self.assertEqual(actual_output, expected_output)

        H1 = graph.addVertex('H1', 3, 10)
        actual_output = graph.getVerticesCount()
        expected_output = 3
        self.assertEqual(actual_output, expected_output)

    # Test the current value of the Fund
    def test_currentValue(self):
        graph = self.graph
        Inv1 = graph.addVertex('Inv1', 1)
        Inv2 = graph.addVertex('Inv2', 1)
        F1 = graph.addVertex('F1', 2)
        F2 = graph.addVertex('F2', 2)
        F3 = graph.addVertex('F3', 2)
        H1 = graph.addVertex('H1', 3, 10)
        H2 = graph.addVertex('H2', 3, 20)
        H3 = graph.addVertex('H3', 3, 15)
        H4 = graph.addVertex('H4', 3, 10)
        graph.addEdge((Inv1, F1))
        graph.addEdge((Inv1, F2))
        graph.addEdge((F1, H1), 100)
        graph.addEdge((F1, H2), 100)
        graph.addEdge((F1, H4), 100)
        graph.addEdge((F2, H1), 100)
        graph.addEdge((F2, H3), 100)

        # Checking value of fund 1
        actual_output = graph.getFundValue(F1)
        expected_output = 4000
        self.assertEqual(actual_output, expected_output)

        # Checking value of Investor 1
        actual_output = graph.getInvestorValue(Inv1)
        expected_output = 6500
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
