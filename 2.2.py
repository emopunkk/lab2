def split_list_by_value(items, pivot_value):
    less_list = []
    greater_or_equal_list = []

    for item in items:
        if item < pivot_value:
            less_list.append(item)
        else:
            greater_or_equal_list.append(item)

    print("\nРезультат роботи функції")
    print("Початковий список:", items)
    print(f"Список 1 (елементи < {pivot_value}):", less_list)
    print(f"Список 2 (елементи >= {pivot_value}):", greater_or_equal_list)

    return less_list, greater_or_equal_list

# ГОЛОВНИЙ БЛОК ПРОГРАМИ
if __name__ == "__main__":
    # Введення списку з клавіатури
    while True:
        try:
            raw_input = input("Введіть елементи списку (числа через пробіл): ").strip()
            if not raw_input:
                print("Помилка, Список не може бути порожнім\n")
                continue
            # Перетворюємо введені рядки у числа (int або float)
            user_list = [float(x) if '.' in x else int(x) for x in raw_input.split()]
            break
        except ValueError:
            print("Помилка вводьте лише числові значення, розділені пробілом\n")

    # Введення значення для розбиття
    while True:
        try:
            raw_val = input("Введіть значення елемента для розбиття: ").strip()
            split_val = float(raw_val) if '.' in raw_val else int(raw_val)
            break
        except ValueError:
            print("Помилка введіть коректне числове значення\n")

    # Виклик функції
    split_list_by_value(user_list, split_val)

    # Затримка закриття консолі
    input("\nНатисніть Enter, щоб закрити програму...")