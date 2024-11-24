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

def json_to_csv():
    try:
        # Зчитування даних з .json файлу
        with open(json_filename, mode="r", encoding="utf-8") as json_file:
            json_data = json.load(json_file)

        # Додаємо кілька нових рядків до даних
        new_data = [
            {"ID": 6, "First name": "Frank", "Second name": "Miller", "Age": 22, "Grade": "B", "Country": "France"},
            {"ID": 7, "First name": "Grace", "Second name": "Lee", "Age": 23, "Grade": "A-", "Country": "Italy"}
        ]

        # Додаємо нові рядки до основних даних
        json_data.extend(new_data)

        # Перезаписуємо .json файл з новими даними
        with open(json_filename, mode="w", encoding="utf-8") as json_file:
            json.dump(json_data, json_file, ensure_ascii=False, indent=4)

        print(f"Нові дані успішно додано в {json_filename}.")

        # Тепер перетворюємо оновлений JSON файл у CSV
        with open(csv_filename, mode="w", newline="", encoding="utf-8") as csv_file:
            # Отримуємо заголовки з першого запису
            fieldnames = json_data[0].keys() if json_data else []
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(json_data)

        print(f"Дані успішно переписано з {json_filename} до {csv_filename}.")

    except FileNotFoundError:
        print(f"Файл {json_filename} не знайдено.")
    except Exception as e:
        print(f"Помилка при обробці файлів: {e}")

if __name__ == "__main__":
    create_csv_file()
    csv_to_json()
    json_to_csv()
