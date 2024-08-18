import sys
from pathlib import Path

# Get the absolute path of the main_project directory
main_project_path = Path(__file__).resolve().parent.parent.parent

# Add the main_project directory to sys.path
sys.path.append(str(main_project_path))


class Solution:
    """
    A class that provides solutions for operations on a stack.

    Attributes:
        stack (LinkedList): The linked list to perform operations on.
    """