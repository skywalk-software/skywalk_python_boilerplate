from skywalk_example.utils import example_function


def test_example_function():
    assert example_function(2, 3) == 5
    assert example_function(-1, 1) == 0
    assert example_function(0, 0) == 0
