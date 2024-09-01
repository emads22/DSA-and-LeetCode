## 1. Convert Sorted List to Balanced BST (**Interview Question**)

### Develop a method that takes a sorted list of integers as input and constructs a height-balanced BST.

This involves creating a BST where the depth of the two subtrees of any node does not differ by more than one.

Achieving a height-balanced tree is crucial for optimizing the efficiency of tree operations, ensuring that the BST remains efficient for search, insertion, and deletion across all levels of the tree.

### Method Overview: `__sorted_list_to_bst`

- **Input:**  
  A sorted list of integers `nums`, provided in ascending order. The input list represents a sequential collection of elements to be transformed into a BST. The method also receives two additional parameters, `left` and `right`, which denote the current segment of the list being processed.

- **Process:**  
  The method `__sorted_list_to_bst` employs a divide-and-conquer strategy to construct the BST. It identifies the middle element of the current list segment to serve as the subtree's root, ensuring that the resulting BST is height-balanced. The method recursively applies this logic to the left and right halves of the list, building up the BST from the bottom up.

- **Output:**  
  The root node of a height-balanced BST constructed from the sorted list. This node links to all other nodes in the BST, effectively representing the entire tree structure.

### Requirements:

- The BST must maintain the binary search tree property: for any given node, all values in the left subtree must be less than the node's value, and all values in the right subtree must be greater.
- The resulting BST should be height-balanced to optimize the efficiency of subsequent operations performed on the tree.

### Implementation Details:

- The class `BinarySearchTree` encapsulates the functionality needed to construct and manage a BST, including the method `sorted_list_to_bst` which serves as the public interface for converting a sorted list into a BST.
- The method `__sorted_list_to_bst` is a recursive helper function designed for internal use within the class. It directly supports the construction process by dividing the list and building the tree to ensure it is height-balanced.

-----------------------------------------------------------------------------------------



## 2. Invert Binary Tree (**Interview Question**) 

### Write a method `__invert_tree(self, node)` to invert (or mirror) a binary tree. This means that for every node in the binary tree, you will swap its left and right children.

#### Input:
- **node**: A Node object representing the root of a binary tree. The Node class has attributes value, left, and right, where value is the value stored in the node, and left and right are pointers to the node's left and right children, respectively.

#### Output:
- The root node of the inverted binary tree.

#### Requirements:
- The method must be recursive. It should work by traversing the tree and swapping the left and right children of every node encountered.
- If the input tree is empty (i.e., node is None), the method should return None.
- The inversion should happen in-place, meaning you should not create a new tree but instead modify the existing tree structure.
- The method should handle binary trees of any size and structure, ensuring that every node's left and right children are swapped.

#### Example:

**Given a binary tree structured as follows**:

```
    47
   /  \
  23   77
 / \   / \
15  35 60 90
```

**After calling __invert_tree(root), where root is the node with the value 47, the tree should be inverted to look like this:**

```
    47
   /  \
  77   23
 / \   / \
90 60 35 15
```

**Note**:
This problem requires understanding binary trees, recursion, and the ability to manipulate tree nodes directly. The solution should ensure that every node's left and right children are swapped all the way down the tree, effectively creating a mirror image of the original structure.

-----------------------------------------------------------------------------------------



## 3. Validate BST (**Interview Question**)

### Write a method called `is_valid_bst` in the `BinarySearchTree` class that checks whether a binary search tree is a valid binary search tree.

Your method should use the `dfs_in_order` method to get the node values of the binary search tree in ascending order, and then check whether each node value is greater than the previous node value.

- If the node values are not sorted in ascending order, the method should return `False`, indicating that the binary search tree is not valid.
- If all node values are sorted in ascending order, the method should return `True`, indicating that the binary search tree is a valid binary search tree.

**Key Points**:
- Use the dfs_in_order method to traverse the tree and collect node values.
- Validate that the collected node values are in strictly ascending order.
- Return True if valid, otherwise False.

-----------------------------------------------------------------------------------------



## 4. Kth Smallest Node (**Interview Question**)

### Given a binary search tree, write a method `find_kth_smallest(self, k)` that finds the kth smallest element in the tree. For example, if the tree contains the elements `[1, 2, 3, 4, 5]`, the 3rd smallest element would be `3`.

The solution to this problem usually involves traversing the tree in-order (left, root, right) and keeping track of the number of nodes visited until you find the kth smallest element. There are two main approaches to doing this:

1. **Iterative Approach Using a Stack:**
   - This approach involves maintaining a stack of nodes that still need to be visited, starting with the leftmost node.
   - At each step, you pop a node off the stack, decrement the kth smallest counter, and check whether you have found the kth smallest element.
   - If you have not, you continue traversing the tree by moving to the right child of the current node.

2. **Recursive Approach:**
   - This approach involves recursively traversing the tree in-order and keeping track of the number of nodes visited until you find the kth smallest element.
   - You can use a helper function that takes a node and a value of `k` as input, and recursively calls itself on the left and right children of the node until it finds the kth smallest element.

Both of these approaches have their own advantages and disadvantages, and the best approach to use may depend on the specific problem constraints and the interviewer's preferences.

**Key Points**:
- Use in-order traversal to get elements in ascending order.
- Maintain a count of nodes visited to determine the kth smallest.
- Choose between iterative (stack-based) or recursive approach based on context and requirements.

-----------------------------------------------------------------------------------------
