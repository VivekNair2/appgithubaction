import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.mathoperation import add, subtract

def test_add():
    assert add(2, 3) == 5
    assert add(-2, 3) == 1

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-2, 3) == -5