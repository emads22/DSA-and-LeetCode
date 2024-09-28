# Common Search Algorithms

### 1. Linear Search
   - **Description**: A simple algorithm that checks each element in the list sequentially until the target value is found or the list ends. It does not require the list to be sorted.
   - **Time Complexity**: O(n)
   - **Space Complexity**: O(1) (iterative) or O(n) (recursive due to call stack)
   - **Best Use Case**: Searching for an element in an unsorted or small list where simplicity is preferred over efficiency.

### 2. Binary Search
   - **Description**: An efficient algorithm for finding an item from a sorted list. It repeatedly divides the search interval in half, checking if the target value is in the left or right half.
   - **Time Complexity**: O(log n)
   - **Space Complexity**: O(1) (iterative) or O(log n) (recursive due to call stack)
   - **Best Use Case**: Searching for an element in a large, sorted array or list.

### 3. Breadth-First Search (BFS)  
- **Description**: A tree or graph traversal algorithm that explores all the neighbor nodes at the present depth prior to moving on to nodes at the next depth level. Often implemented using a queue.  
- **Time Complexity**: O(V + E), where V is the number of vertices and E is the number of edges in the graph. For trees, this simplifies to O(V), where V is the number of nodes.  
- **Space Complexity**: O(V) (for storing the queue and visited nodes). BFS generally uses more memory than DFS due to the need to store multiple nodes at the same depth level in its queue.  
- **Best Use Case**: Finding the shortest path in unweighted graphs or trees, or exploring all nodes layer by layer.  

### 4. Depth-First Search (DFS)  
- **Description**: A tree or graph traversal algorithm that explores as far down a branch as possible before backtracking. It can be implemented using recursion or a stack.  
- **Time Complexity**: O(V + E), where V is the number of vertices and E is the number of edges in the graph. For trees, this also simplifies to O(V), where V is the number of nodes.  
- **Space Complexity**: O(V) (for storing the visited nodes) or O(h) for the recursive stack, where h is the height of the tree/graph. DFS can use less memory in deep trees or graphs but may require more memory in wide graphs or when implemented iteratively with a stack.  
- **Best Use Case**: Finding the longest path in directed acyclic graphs, exploring all possible paths, solving puzzles, and searching through a maze.  

#### When to Use BFS or DFS:
- **If you know a solution is not far from the root of the tree**: 
    - **BFS**
- **If the tree is very deep and solutions are rare**: 
    - **BFS - (DFS will be slower)**
- **If the tree is very wide**: 
    - **DFS - (BFS will need too much memory in a queue)**
- **If solutions are frequent but located deep in the tree**: 
    - **DFS**
- **Determining whether a path exists between two nodes**: 
    - **DFS**
- **Finding the shortest path**: 
    - **BFS** 

### 5. Bellman-Ford Algorithm 
- **Description**: An algorithm for finding the shortest path from a single source vertex to all other vertices in a weighted graph. It can handle graphs with negative weight edges.  
- **Time Complexity**: O(V * E), where V is the number of vertices and E is the number of edges.  
- **Space Complexity**: O(V) (for storing the distance from the source to each vertex).  
- **Best Use Case**: Useful when the graph contains negative weight edges.

### 6. Dijkstra's Algorithm
- **Description**: An algorithm for finding the shortest path from a single source vertex to all other vertices in a graph with non-negative edge weights. It uses a priority queue to explore the nearest vertex.  
- **Time Complexity**: O((V + E) log V) with a priority queue (using a binary heap).  
- **Space Complexity**: O(V) (for storing the distances from the source).  
- **Best Use Case**: Ideal for graphs with non-negative weights, such as road networks.

