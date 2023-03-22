from modules.graph_node import GraphNode

network = []  # this contains all graphNodes


# Helper function to find node

def find_node(nodeData):
    for _node in network:
        if _node.data == nodeData:
            return _node

    else:
        print("Node not found!")


# Recursive function to find path between two nodes and include it in the path
def find_path(s_node: GraphNode, e_node: GraphNode, possible_path: list):
    possible_path.append(s_node)
    if s_node.data == e_node.data:
        return True
    for _neighbour in s_node.neighbours:
        if _neighbour not in possible_path:
            if find_path(_neighbour, e_node, possible_path):
                return True
    possible_path.pop()
    return False


while True:
    print("1. Insert Graph Node")
    print("2. View all Graph Nodes")
    print("3. Add Neighbour")
    print("4. Find Path")
    print("5. Test Cases")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        data = input("\nEnter node name: ")
        myNode = GraphNode(data)
        network.append(myNode)
        print("Node added successfully!\n")

    elif choice == "2":
        for node in network:
            print("Graph Node: ", node.show_data())
            node.show_neighbours()

    elif choice == "3":

        selectedNode = input("\nEnter node name to add neighbours (case sensitive) : ")
        for node in network:
            if node.show_data() == selectedNode:
                index_of_node = network.index(node)
                updated_node = GraphNode(node.data, node.neighbours)
                print("List of Graph Nodes that can be added as neighbour")
                for n in network:
                    print(n.data)
                while True:
                    neighbour = input("\nEnter a GraphNode from above as neighbour of selected node (or 'done' to "
                                      "finish): ")
                    if neighbour == 'done':
                        break
                    # Find the GraphNode object corresponding to the input and add it as a neighbour
                    neighbour_node = find_node(neighbour)
                    if neighbour_node:
                        updated_node.insert_neighbour(neighbour_node)
                    else:
                        print("Invalid node name. Please try again.")
                        continue
                network[index_of_node] = updated_node
                print("\nNeighbours added successfully! \n")
                break


    elif choice == "4":
        start = input("\nEnter the name of starting node: ")
        end = input("Enter the name of ending node: ")

        startNode = find_node(start)
        endNode = find_node(end)

        # checking if both nodes are valid nodes
        if startNode is None or endNode is None:
            print("One or both nodes are invalid")
            break

        # check if there is a direct path between two nodes
        if endNode in startNode.neighbours:
            print("Direct path found between two nodes given")

        # List to hold the path between two Graph Nodes
        path = []

        # boolean flag found to set if node is found
        found = find_path(startNode, endNode, path)

        if found:
            print("Following path found between two nodes:")
            for p in path:
                print(p)
        else:
            print("No possible path found")

    elif choice == "5":
        objA = GraphNode("A")
        objB = GraphNode("B")
        objC = GraphNode("C")
        objD = GraphNode("D")

        objA.insert_neighbour(objC)
        objC.insert_neighbour(objD)

        path_list = []
        found_path = find_path(objA, objD, path_list)
        print("Path found:", found_path)
        for p in path_list:
            print(p)

    elif choice == "0":
        break

    else:
        print("Invalid choice. Please try again.")
