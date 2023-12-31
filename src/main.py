from src.functions import after_of_operations

from src.functions import load_operations

from src.functions import slices_by_operation

for date in after_of_operations():
    for operation in load_operations():
        if "date" not in operation:
            continue

        elif str(date) in operation["date"]:
            if "from" not in operation:
                print(f'{date.strftime("%d.%m.%Y")} {operation["description"]}\n'
                      f'{slices_by_operation(operation["to"])}\n{operation["operationAmount"]["amount"]} '
                      f'{operation["operationAmount"]["currency"]["name"]}\n')

            else:
                from_operation = operation["from"][-16:-12]
                print(f'{date.strftime("%d.%m.%Y")} {operation["description"]}\n'
                      f'{slices_by_operation(operation["from"])} -> {slices_by_operation(operation["to"])}\n'
                      f'{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n')
