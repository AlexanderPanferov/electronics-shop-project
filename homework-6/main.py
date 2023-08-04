from src.items import Item

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv('missing_file')
    # FileNotFoundError: Отсутствует файл items.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv('corrupted_file.csv')
    # InstantiateCSVError: Файл items.csv поврежден
