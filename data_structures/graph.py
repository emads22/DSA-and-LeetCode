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
        Return a string representation of the graph.

        Returns:
            str: The string representation of the graph.
        """
        display = "\n\n*  "
        if not self.adj_list:
            display += "\n None"
        for vertex, adjacents in self.adj_list.items():
            display += f"\n . '{vertex}' | {adjacents}"
        display += "\n\n"
        return display

    def display(self) -> None:
        """
        Print the string representation of the graph.
        """
        print(self)

    def empty(self) -> bool:
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
