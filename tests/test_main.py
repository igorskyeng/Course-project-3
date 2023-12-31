from src.main import input_operation


def test_input_operation():
    assert input_operation('test_operations.json') != ''
