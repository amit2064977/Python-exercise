from pprint import pprint

class Vertex:
    def __init__(self, name, value=0):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"{self.name}"


class Edge:
    def __init__(self, vertex1, vertex2, weight=0):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight

    def displayEdge(self):
        # Display Edges details
        return f"{self.vertex1.name}--{self.weight}-->{self.vertex2.name}"



class Graph:
    def __init__(self):
        # GRAPH VERTICES
        self.vertices = {}

    def addVertex(self, name, level, value=0):
        '''Add vertex in graph
            INPUT: {
                name : vertex name --> string
                level : level to which vertex needs to be added lies between [1, 2, 3] --> int
                value: DEFAULT but required while adding the vertex on level 3 --> int
            }
            OUTPUT: {
                vertex : newly created vertex object
            }
        '''
        # Checking if the level value doesn't lie between 1 to 3 than raising an error

        if level < 1 or level > 3:
            raise ValueError('Level value out of bounds. It should be between 1 to 3')
        if level == 3:
            # If value is not provided
            if value == 0:
                raise ValueError('Please Enter holding value')
        vertex = Vertex(name, value)
        # Adding the vertex to the graph vertices
        self.vertices[vertex] = []
        return vertex



    def addEdge(self, pair, weight=0):
        '''Add relationship between two vertices i.e Edge
        INPUT: {
            pair : Pair of vertices --> tuple
            weight: DEFAULT i.e 0 --> int
        }
        '''
        try:
            edge = self._createEdge(pair, weight)
            if edge.vertex1 not in self.vertices:
                self.vertices[edge.vertex1] = []
            if edge.vertex2 not in self.vertices:
                self.vertices[edge.vertex2] = []
            self.vertices[edge.vertex1].append((edge.vertex2, weight))
        except Exception as e:
            print('Exception in addEdge: ', str(e))

    def _createEdge(self, edge_pair, weight):
        '''Creates Edge Object'''
        parent, child = edge_pair
        edge = Edge(parent, child, weight)
        return edge


    def displayGraph(self):
        '''Displays Graph structure'''
        return self.vertices

    def getVerticesCount(self):
        '''Display number of vertices present in the graph'''
        return len(self.vertices)

    def getFundValue(self, fund):
        '''Returns current value of fund'''
        value = self._getCurrentValue(fund, weight=0, value=0)
        return value

    def getInvestorValue(self, investor):
        '''Returns current value of Investor'''
        value = self._getCurrentValue(investor, weight=0, value=0)
        return value

    def _getCurrentValue(self, node, weight=0, value=0):
        '''Returns the current total value of a Fund
            INPUT: {
                node : Fund/Investor --> vertex object
                weight : DEFAULT i.e 0 --> int
                value : DEFAULT i.e 0 --> int
            }
            OUTPUT: {
                value : Total value of a Fund/Investor
            }
        '''
        # BASE CASE
        try:
            if self.vertices.get(node, []) == []:
                return value + (node.value) * weight
            else:
                for v, w in self.vertices[node]:
                    # Recursive Call
                    value = self._getCurrentValue(v, w, value)
                return value
        except Exception as e:
            print('Exception in  _getCurrentValue: ', str(e))


def main():
    graph = Graph()
    # Investors
    Inv1 = graph.addVertex('Inv1', 1)
    Inv2 = graph.addVertex('Inv2', 1)

    # Funds
    F1 = graph.addVertex('F1', 2)
    F2 = graph.addVertex('F2', 2)
    F3 = graph.addVertex('F3', 2)

    # Holdings
    H1 = graph.addVertex('H1', 3, 10)
    H2 = graph.addVertex('H2', 3, 20)
    H3 = graph.addVertex('H3', 3, 15)
    H4 = graph.addVertex('H4', 3, 10)

    # Adding Edges
    graph.addEdge((Inv1, F1))
    graph.addEdge((Inv1, F2))

    # Assuming quantity as 100 for all holdings
    graph.addEdge((F1, H1), 100)
    graph.addEdge((F1, H2), 100)
    graph.addEdge((F1, H4), 100)
    graph.addEdge((F2, H1), 100)
    graph.addEdge((F2, H3), 100)

    # Investor 2 Edges
    graph.addEdge((Inv2, F2))
    graph.addEdge((Inv2, F3))
    graph.addEdge((F3, H1), 100)
    graph.addEdge((F3, H4), 100)

    pprint(graph.displayGraph(), indent=4)
    print("Current value of Fund F1: ", graph.getFundValue(F1))
    print("Current value of Fund Inv1: ", graph.getInvestorValue(Inv1))


if __name__ == '__main__':
    main()

