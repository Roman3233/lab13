import csv
import json

csv_data = [
    ["ID", "First name", "Second name", "Age", "Grade", "Country"],
    [1, "Alice", "Johnson", 20, "A", "USA"],
    [2, "Bob", "Smith", 18, "B", "UK"],
    [3, "Charlie", "Brown", 18, "A+", "Canada"],
    [4, "Diana", "Evans", 19, "B-", "Australia"],
    [5, "Edward", "Taylor", 21, "C", "USA"]
]
csv_filename = "data.csv"
json_filename = "data.json"

# Функція для запису даних у .csv файл
def create_csv_file():
    try:
        with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(csv_data)
            print(f"Дані успішно записано в {csv_filename}.")
    except Exception as e:
        print(f"Помилка при створенні або записі у .csv файл: {e}")

# Функція для зчитування та запису даних
def csv_to_json():
    try:
        # Зчитування .csv
        with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            json_data = [row for row in csv_reader]
        # Запис у .json
        with open(json_filename, mode="w", encoding="utf-8") as json_file:
            json.dump(json_data, json_file, ensure_ascii=False, indent=4)
            print(f"Дані успішно переписано з {csv_filename} до {json_filename}.")
    except FileNotFoundError:
        print(f"Файл {csv_filename} не знайдено.")
    except Exception as e:
        print(f"Помилка при обробці файлів: {e}")

if __name__ == "__main__":
    create_csv_file()
    csv_to_json()