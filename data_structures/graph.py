from typing import TypeVar, Generic


ItemType = TypeVar('ItemType')


class Graph(Generic[ItemType]):
    """
    A simple, undirected graph implementation using an adjacency list.

    Attributes:
        adj_list (dict): A dictionary where keys are vertices and values are lists
                         of adjacent vertices.
    """

    def __init__(self) -> None:
        """
        Initialize an empty graph.
        """
        self.adj_list: dict = {}

    def __repr__(self) -> str:
        """
        Return a concise string representation of the graph.

        Returns:
            str: A string representation of the graph.
        """
        return f"Graph(Vertices: {len(self.adj_list)}, Adjacency List: {self.adj_list})"

    def __str__(self) -> str:
        """
        Return a formatted string representation of the graph.

        Returns:
            str: The string representation of the graph.
        """
        display = "\n*  "
        if not self.adj_list:
            display += "\tNone\n"
        for vertex, adjacents in self.adj_list.items():
            display += f"\t. '{vertex}' | {adjacents}\n"
        return display

    def display(self) -> None:
        """
        Print the string representation of the graph.
        """
        print(str(self))

    def is_empty(self) -> bool:
        """
        Check if the graph is empty.

        Returns:
            bool: True if the graph is empty, False otherwise.
        """
        return len(self.adj_list) == 0

    def add_vertex(self, vertex: ItemType) -> bool:
        """
        Add a vertex to the graph.

        Args:
            vertex (ItemType): The vertex to add to the graph.

        Returns:
            bool: True if the vertex was added, False if it already existed.
        """
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    def remove_vertex(self, vertex: ItemType) -> bool:
        """
        Remove a vertex and all associated edges from the graph.

        Args:
            vertex (ItemType): The vertex to remove from the graph.

        Returns:
            bool: True if the vertex was removed, False if it did not exist.
        """
        if vertex in self.adj_list:
            # Remove the vertex from the adjacency lists of all other vertices
            for v in self.adj_list[vertex]:
                self.adj_list[v].remove(vertex)
            # Remove the vertex itself
            del self.adj_list[vertex]
            return True
        return False

    def add_edge(self, vertex1: ItemType, vertex2: ItemType) -> bool:
        """
        Add an undirected edge between two vertices.

        Args:
            vertex1 (ItemType): The first vertex.
            vertex2 (ItemType): The second vertex.

        Returns:
            bool: True if the edge was added, False if one or both vertices do not exist.
        """
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            # Add each vertex to the other's adjacency list
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)
            return True
        return False

    def remove_edge(self, vertex1: ItemType, vertex2: ItemType) -> bool:
        """
        Remove an undirected edge between two vertices.

        Args:
            vertex1 (ItemType): The first vertex.
            vertex2 (ItemType): The second vertex.

        Returns:
            bool: True if the edge was removed, False if one or both vertices do not exist
                  or if the edge does not exist.
        """
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            try:
                # Remove each vertex from the other's adjacency list
                self.adj_list[vertex1].remove(vertex2)
                self.adj_list[vertex2].remove(vertex1)
                return True
            except ValueError:
                # Edge does not exist
                pass
        return False


def main():
    # Create a new graph
    graph = Graph[str]()

    # Display the initial graph (should be empty)
    print("Initial graph:")
    graph.display()
    print("-" * 60)

    # Add vertices
    print("\n==> Test: add_vertex()")
    print("\n\t- Adding vertices 'A', 'B', 'C':\n")
    print(f"\t\t. Added 'A': {graph.add_vertex('A')}")
    print(f"\t\t. Added 'B': {graph.add_vertex('B')}")
    print(f"\t\t. Added 'C': {graph.add_vertex('C')}")

    # Display the graph
    graph.display()
    print("-" * 60)

    # Add edges
    print("\n==> Test: add_edge()")
    print("\n\t- Adding edges ('A', 'B') and ('B', 'C'):\n")
    print(f"\t\t. Added edge ('A', 'B'): {graph.add_edge('A', 'B')}")
    print(f"\t\t. Added edge ('B', 'C'): {graph.add_edge('B', 'C')}")

    # Display the graph
    graph.display()
    print("-" * 60)

    # Remove an edge
    print("\n==> Test: remove_edge()")
    print("\n\t- Removing edge ('A', 'B'):\n")
    print(f"\t\t. Removed edge ('A', 'B'): {graph.remove_edge('A', 'B')}")

    # Display the graph
    graph.display()
    print("-" * 60)

    # Remove a vertex
    print("\n==> Test: remove_vertex()")
    print("\n\t- Removing vertex 'B':\n")
    print(f"\t\t. Removed 'B': {graph.remove_vertex('B')}")

    # Display the graph
    graph.display()
    print("-" * 60)

    # Check if the graph is empty
    print("\n==> Test: is_empty()")
    print(f"\n\t. Is the graph empty? {graph.is_empty()}\n")
    print("-" * 60)

    # Attempt to add a vertex that already exists
    print("\n==> Test: add_vertex()")
    print("\n\t. Adding vertex 'A' again:\n")
    print(f"\t\t. Added 'A': {graph.add_vertex('A')}")

    # Display the graph
    graph.display()
    print("-" * 60)


if __name__ == "__main__":
    main()
