def add_digits_to_set():
    # Початкова множина символів
    symbols_set = {'c', 'd'}
    # Множина усіх цифр (символи від '0' до '9')
    digits_set = set("0123456789")
    print("Початкова множина символів:", symbols_set)
    print("Множина усіх цифр:", digits_set)
    # Додаємо множину цифр до початкової множини
    symbols_set.update(digits_set)
    
    print("Результуюча множина:", symbols_set)
    return symbols_set
if __name__ == "__main__":
    add_digits_to_set()
    # Затримка закриття консолі
    input("\nНатисніть Enter, щоб закрити програму...")