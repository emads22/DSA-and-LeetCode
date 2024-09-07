## 1. Merge Two Sorted LL (**Interview Question**)

### Implement the `merge` method within the `LinkedList` class. The `merge` method takes in another LinkedList as an input and merges it with the current LinkedList. The elements in both lists are assumed to be in ascending order.

**Parameters**

- `other_list` (LinkedList): the other LinkedList to merge with the current list.

**Return Value**

This method does not return a value, but it modifies the current LinkedList to contain the merged list.

**Example:**

```python
l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)
 
l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)
 
l1.merge(l2)
# The current list (l1) now contains the merged list [1, 2, 3, 4, 5, 6, 7, 8]
```

**Detailed Steps:**

1. **Initialize Helper Nodes**:
   - Create a "dummy" node that acts as a starting point, and give it a value of 0.
   - Create another node called "current" and set it to point to this dummy node. We'll use "current" to keep track of where we are in the new merged list.

2. **Merge Loop**:
   - This loop will go through each node in both the list we're working on (`self.head`) and the list we're merging into it (`other_head`).
   - For each pair of nodes (one from each list), compare their values.
   - Take the node with the smaller value and attach it to the "current" node.
   - Move both the "current" node and the list head that had the smaller value to their respective next nodes.

3. **Check for Remaining Nodes**:
   - After the loop, it's possible that one list still has nodes while the other doesn't.
   - If that's the case, take the remaining nodes from the list that isn't empty and attach them to "current".

4. **Update Head, Tail, and Length**:
   - Once you're done with the merging, the "dummy" node will still be at the start. Update the head of the list to point to the node that comes immediately after this dummy node.
   - Also, make sure to update the tail node to be the last node in the new, merged list.
   - Finally, update the length of the list to account for the nodes from both original lists.

-----------------------------------------------------------------------------------------

