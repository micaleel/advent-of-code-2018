import pytest
from puzzle_1 import *

def test_ex1_p2():
    """
    First reach returns correct frequency
    """
    assert get_first_reach([+1, -1]) == 0
    assert get_first_reach([+3, +3, +4, -2, -4]) == 10
    assert get_first_reach([-6, +3, +8, +5, -6]) == 5
    assert get_first_reach([+7, +7, -2, -7, -4]) == 14
