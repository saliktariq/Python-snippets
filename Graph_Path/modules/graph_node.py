class GraphNode:
    def __init__(self, data, neighbours=None):
        self.data = data
        if neighbours is None:
            self.neighbours = []
        else:
            self.neighbours = neighbours

    def insert_neighbour(self, neighbour):
        self.neighbours.append(neighbour)

    def show_data(self):
        return self.data

    def show_neighbours(self):
        print("Neighbours: ")
        for n in self.neighbours:
            print(n)

    def __str__(self):
        return self.data



