from src.functions import load_operations

from src.functions import after_of_operations

from src.functions import slices_by_operation


def test_load_operations():
    assert load_operations('test_operations.json')


def test_after_of_operations():
    assert after_of_operations(load_operations('test_operations.json'), -5)


def test_slices_by_operation():
    for date in after_of_operations(load_operations('test_operations.json'), -35):
        for operation in load_operations('test_operations.json'):
            if "date" not in operation:
                continue

            elif str(date) in operation["date"]:
                if "from" not in operation:
                    assert slices_by_operation(operation["to"])

                else:
                    assert slices_by_operation(operation["from"])
                    assert slices_by_operation(operation["to"])
