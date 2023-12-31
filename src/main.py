from src.functions import after_of_operations

from src.functions import load_operations

from src.functions import slices_by_operation


def input_operation(file='operations.json'):
    """
    Выводит пользователю 5 псоедних выполненных банковских операций
    """

    # Скрывает скрип функции от запуска при импорте в "test_main.py"
    if __name__ == "__main__":

        # Итерирует даты 5 последних банковских операций
        for date in after_of_operations(load_operations(file)):

            # Итерирует все банковские операции
            for operation in load_operations(file):

                # Пропускает банковские операции при отсутствии даты
                if "date" not in operation:
                    continue

                elif str(date) in operation["date"]:

                    # Вывод открытия банковской операции
                    if "from" not in operation:
                        print(f'{date.strftime("%d.%m.%Y")} {operation["description"]}\n'
                              f'{slices_by_operation(operation["to"])}\n{operation["operationAmount"]["amount"]} '
                              f'{operation["operationAmount"]["currency"]["name"]}\n')

                    # Вывод перевода банковской операции
                    else:
                        print(f'{date.strftime("%d.%m.%Y")} {operation["description"]}\n'
                              f'{slices_by_operation(operation["from"])} -> {slices_by_operation(operation["to"])}\n'
                              f'{operation["operationAmount"]["amount"]} '
                              f'{operation["operationAmount"]["currency"]["name"]}\n')


input_operation()
