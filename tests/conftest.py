import pytest
import os

@pytest.fixture
def datadir():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")