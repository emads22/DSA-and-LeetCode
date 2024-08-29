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