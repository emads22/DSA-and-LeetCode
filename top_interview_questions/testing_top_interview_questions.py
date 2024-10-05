from top_interview_solutions import Solution
from utils import *


def test_reverseString():
    """Test reverseString with multiple cases."""
    s = Solution()
    tests = [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
    ]

    print("-" * 80)
    print("\n==> Test: reverseString()\n")
    for test_input, expected_output in tests:
        print(f"\t. Before:  {test_input}")
        s.reverseString(test_input)
        assert test_input == expected_output, f"""Test failed. Expected `{
            expected_output}`, got `{test_input}`"""
        print(f"\t. After:   {test_input}  -->  OK\n")
    print("-" * 80)


def test_fizzBuzz():
    """Test fizzBuzz with multiple cases."""
    s = Solution()
    tests = [
        (3, ['1', '2', 'Fizz']),
        (5, ["1", "2", "Fizz", "4", "Buzz"]),
        (15, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8",
         "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]),
    ]

    print("-" * 80)
    print("\n==> Test: fizzBuzz()\n")
    for test_input, expected_output in tests:
        output = s.fizzBuzz(test_input)
        print(f"\t. Input:   {test_input}")
        assert output == expected_output, f"""Test failed. Expected `{
            expected_output}`, got `{output}`"""
        print(f"\t. Output:  {output}  -->  OK\n")
    print("-" * 80)


def test_singleNumber():
    """Test singleNumber with multiple cases."""
    s = Solution()
    tests = [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1)
    ]

    print("-" * 80)
    print("\n==> Test: singleNumber()\n")
    for test_input, expected_output in tests:
        output = s.singleNumber(test_input)
        print(f"\t. Input:   {test_input}")
        assert output == expected_output, f"""Test failed. Expected `{
            expected_output}`, got `{output}`"""
        print(f"\t. Output:  {output}  -->  OK\n")
    print("-" * 80)


def test_singleNumber():
    """Test singleNumber with multiple cases."""
    s = Solution()
    tests = [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1)
    ]

    print("-" * 80)
    print("\n==> Test: singleNumber()\n")
    for test_input, expected_output in tests:
        output = s.singleNumber(test_input)
        print(f"\t. Input:   {test_input}")
        assert output == expected_output, f"""Test failed. Expected `{
            expected_output}`, got `{output}`"""
        print(f"\t. Output:  {output}  -->  OK\n")
    print("-" * 80)


def test_maxDepth():
    """Test maxDepth with multiple cases."""
    s = Solution()
    tests = [
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2)
    ]

    print("-" * 80)
    print("\n==> Test: maxDepth()\n")
    for test_input, expected_output in tests:
        bt = BinaryTree()
        bt.build_from_list(test_input)
        output = s.maxDepth(bt.root)
        print(f"\t. Input:   {test_input}")
        assert output == expected_output, f"""Test failed. Expected `{
            expected_output}`, got `{output}`"""
        print(f"\t. Output:  {output}  -->  OK\n")
    print("-" * 80)


def test_moveZeroes():
    """Test moveZeroes with multiple cases."""
    s = Solution()
    tests = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0])
    ]

    print("-" * 80)
    print("\n==> Test: moveZeroes()\n")
    for test_input, expected_output in tests:
        print(f"\t. Before:  {test_input}")
        s.moveZeroes(test_input)
        assert test_input == expected_output, f"""Test failed. Expected `{
            expected_output}`, got `{test_input}`"""
        print(f"\t. After:   {test_input}  -->  OK\n")
    print("-" * 80)


def test_getSum():
    """Test getSum with multiple cases."""
    s = Solution()
    tests = [
        ({"a": 1, "b": 2}, 3),
        ({"a": 2, "b": 3}, 5)
    ]

    print("-" * 80)
    print("\n==> Test: getSum()\n")
    for test_input, expected_output in tests:
        print(f"\t. Input:   a = {test_input["a"]},  b = {test_input["b"]}")
        output = s.getSum(a=test_input["a"], b=test_input["b"])
        assert output == expected_output, f"""Test failed. Expected `{
            expected_output}`, got `{output}`"""
        print(f"\t. Output:  {output}  -->  OK\n")
    print("-" * 80)


def test_reverseList():
    """Test reverseList with multiple cases."""
    s = Solution()
    tests = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], [])
    ]

    print("-" * 80)
    print("\n==> Test: reverseList()\n")
    for test_input, expected_output in tests:
        ll = LinkedList()
        ll.build_from_list(test_input)
        print(f"\t. Before:  {test_input}")
        ll.head = s.reverseList(ll.head)  # Reverse the linked list
        output = ll.to_list()  # Get list representation of the reversed list
        assert output == expected_output, f"""Test failed. Expected `{
            expected_output}`, got `{output}`"""
        print(f"\t. After:   {output}  -->  OK\n")
    print("-" * 80)


def test_deleteNode():
    """Test deleteNode with multiple cases."""
    s = Solution()
    tests = [
        ({"head": [4, 5, 1, 9], "node": 5}, [4, 1, 9]),
        ({"head": [4, 5, 1, 9], "node": 1}, [4, 5, 9])
    ]
    print("-" * 80)
    print("\n==> Test: deleteNode()\n")
    for test_input, expected_output in tests:
        ll = LinkedList()
        ll.build_from_list(test_input["head"])
        print(f"""\t. Before:  {test_input["head"]},  Node to delete = {
              test_input["node"]}""")
        node_to_delete = ll.get_node(test_input["node"])
        s.deleteNode(node_to_delete)  # Delete the node
        output = ll.to_list()  # List representation of after delete
        assert output == expected_output, f"""Test failed. Expected `{
            expected_output}`, got `{output}`"""
        print(f"\t. After:   {output}  -->  OK\n")
    print("-" * 80)


def test_inorderTraversal():
    """Test inorderTraversal with multiple cases."""
    s = Solution()
    tests = [
        ([1, None, 2, 3], [1, 3, 2]),
        ([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9], [4, 2, 6, 5, 7, 1, 3, 9, 8]),
        ([], []),
        ([1], [1])
    ]

    print("-" * 80)
    print("\n==> Test: inorderTraversal()\n")
    for test_input, expected_output in tests:
        bt = BinaryTree()
        bt.build_from_list(test_input)
        output = s.inorderTraversal(bt.root)
        print(f"\t. Input:   {test_input}")
        assert output == expected_output, f"""Test failed. Expected `{
            expected_output}`, got `{output}`"""
        print(f"\t. Output:  {output}  -->  OK\n")
    print("-" * 80)


def test_titleToNumber():
    """Test titleToNumber with multiple cases."""
    s = Solution()
    tests = [
        ("A", 1),
        ("AB", 28),
        ("ZY", 701)
    ]

    print("-" * 80)
    print("\n==> Test: titleToNumber()\n")
    for test_input, expected_output in tests:
        print(f"\t. Input:   {test_input}")
        output = s.titleToNumber(test_input)
        assert output == expected_output, f"""Test failed. Expected `{
            expected_output}`, got `{output}`"""
        print(f"\t. Output:  {output}  -->  OK\n")
    print("-" * 80)


def test_reverseBits():
    """Test reverseBits with multiple cases."""
    s = Solution()
    tests = [
        ((43261596, "00000010100101000001111010011100"),
         (964176192, "00111001011110000010100101000000")),
        ((4294967293, "11111111111111111111111111111101"),
         (3221225471, "10111111111111111111111111111111"))
    ]

    print("-" * 80)
    print("\n==> Test: reverseBits()\n")
    for test_input, expected_output in tests:
        n, binary = test_input
        print(f"\t. Input:   n = {n},  binary = {binary}")
        output = s.reverseBits(n)
        n_expected, binary_expected = expected_output
        assert output == n_expected, f"""Test failed. Expected `{
            n_expected} (binary = {binary_expected})`, got `{output} (binary = {int_to_bin(output)})`"""
        print(f"""\t. Output:  n = {output},  binary = {
              int_to_bin(output)}  -->  OK\n""")
    print("-" * 80)


def test_reverse():
    """Test reverse with multiple cases."""
    s = Solution()
    tests = [
        (123, 321),
        (-123, -321),
        (120, 21)
    ]

    print("-" * 80)
    print("\n==> Test: reverse()\n")
    for test_input, expected_output in tests:
        print(f"\t. Input:   {test_input}")
        output = s.reverse(test_input)
        assert output == expected_output, f"""Test failed. Expected `{
            expected_output}`, got `{output}`"""
        print(f"""\t. Output:  n = {output}  -->  OK\n""")
    print("-" * 80)


def test_rotate():
    """Test rotate with multiple cases."""
    s = Solution()
    tests = [
        (([1, 2, 3, 4, 5, 6, 7], 3), [5, 6, 7, 1, 2, 3, 4]),
        (([-1, -100, 3, 99], 2), [3, 99, -1, -100])
    ]

    print("-" * 80)
    print("\n==> Test: rotate()\n")
    for test_input, expected_output in tests:
        nums, k = test_input
        print(f"\t. Before:  {nums},  k = {k}")
        s.rotate(nums, k)
        assert nums == expected_output, f"""Test failed. Expected `{
            expected_output}`, got `{nums}`"""
        print(f"""\t. After:   {nums}  -->  OK\n""")
    print("-" * 80)


def test_twoSum():
    """Test twoSum with multiple cases."""
    s = Solution()
    tests = [
        (([2, 7, 11, 15], 9), [0, 1]),
        (([3, 2, 4], 6), [1, 2]),
        (([3, 3], 6), [0, 1])
    ]

    print("-" * 80)
    print("\n==> Test: twoSum()\n")
    for test_input, expected_output in tests:
        nums, target = test_input
        print(f"\t. Input:   {nums},  target = {target}")
        output = s.twoSum(nums, target)
        assert output == expected_output, f"""Test failed. Expected `{
            expected_output}`, got `{output}`"""
        print(f"""\t. Output:  {output}  -->  OK\n""")
    print("-" * 80)


def test_mergeTwoLists():
    """Test mergeTwoLists with multiple cases."""
    s = Solution()
    tests = [
        (([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4]),
        (([], []), []),
        (([], [0]), [0])
    ]

    print("-" * 80)
    print("\n==> Test: mergeTwoLists()\n")
    for test_input, expected_output in tests:
        list1, list2 = test_input
        ll1, ll2, ll3 = LinkedList(), LinkedList(), LinkedList()
        ll1.build_from_list(list1)
        ll2.build_from_list(list2)
        print(f"\t. Input:   List1 = {list1},  List2 = {list2}")
        ll3.head = s.mergeTwoLists(ll1.head, ll2.head)
        output = ll3.to_list()
        assert output == expected_output, f"""Test failed. Expected `{
            expected_output}`, got `{output}`"""
        print(f"""\t. Output:  {output}  -->  OK\n""")
    print("-" * 80)


def main():
    FUNCTIONS = {"1": test_reverseString,
                 "2": test_fizzBuzz,
                 "3": test_singleNumber,
                 "4": test_maxDepth,
                 "5": test_moveZeroes,
                 "6": test_getSum,
                 "7": test_reverseList,
                 "8": test_deleteNode,
                 "9": test_inorderTraversal,
                 "10": test_titleToNumber,
                 "11": test_reverseBits,
                 "12": test_reverse,
                 "13": test_rotate,
                 "14": test_twoSum,
                 "15": test_mergeTwoLists,
                 }

    print("\n\n", "=" * 80)

    while True:
        print("\n")

        for idx, function in FUNCTIONS.items():
            print(f"\t{idx}. {function.__name__}()")

        f_idx = input(
            f"\n\n>>> From the list above, select a function to be tested ('q' for exit):  ")
        print("\n")

        if f_idx in ["q", "Q"]:
            print("=" * 80, "\n")
            break

        try:
            FUNCTIONS[f_idx]()

        except KeyError:
            print("\n--- Invalid input. ---\n")

        except Exception as e:
            print(
                f"\n\n--- Error occurred in `{FUNCTIONS[f_idx].__name__}()`:\n\n\t--> {e} ---\n")


if __name__ == "__main__":
    main()
