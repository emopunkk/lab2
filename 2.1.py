import string
def find_shortest_word_length():
    while True:
        sentence = input("Введіть речення (щонайменше 7 слів): ").strip()
        # Розбиваємо речення на слова та прибираємо розділові знаки по краях кожного слова
        raw_words = sentence.split()
        words = [word.strip(string.punctuation + "«»—–") for word in raw_words]
        # Видаляємо порожні елементи
        words = [word for word in words if word]
        
        if len(words) < 7:
            print(f"Помилка! Ви ввели лише {len(words)} сл. Потрібно щонайменше 7 слів.\n")
        else:
            break
    # Знаходимо найкоротше слово та його довжину
    shortest_word = min(words, key=len)
    min_length = len(shortest_word)
    print(f"Кількість слів у реченні: {len(words)}")
    print(f"Найкоротше слово: «{shortest_word}»")
    print(f"Довжина найкоротшого слова: {min_length}")
# Запуск програми
if __name__ == "__main__":
    find_shortest_word_length()
    input("\nНатисніть Enter, щоб закрити програму...")