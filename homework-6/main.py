from src.items import Item

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv('test1.csv')
    # FileNotFoundError: Отсутствует файл items.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv('test2.csv')
    # InstantiateCSVError: Файл items.csv поврежден
