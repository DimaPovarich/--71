import json
while True:
    file_path = 'qwer.json'
    def print_library(file_path):
        with open(file_path, 'r') as file:
            library = json.load(file)
        print(json.dumps(library, indent=4))

    def add_book(file_path):
        author = (input('Введите имя автора'))
        year = (input('введите год выпуска '))
        name = (input('Введите имя книги'))
        page = (input('количество страниц '))
        data = []
        data.append({"books":[{
                "Name_of_book": str(name),
                "Data_of_create": year,
                "Cout_of_pages": page,
                "Autor": str(author)
            }]})
        with open("qwer.json", "w", encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("Данные о новой книге успешно добавлены!")

    def delete_book(file_path):
        with open("qwer.json", encoding="utf8") as file:
            data = json.load(file)

        data["books"][0].pop("Name_of_book")

        with open("qwer.json", "w", encoding="utf8") as file:
            json.dump(data, file, ensure_ascii=False)

        print_library(file_path)

    #выбор действия
    change = int(input('что вы хотите сделать(1 - добавить книгу, 2 - вывести содержание библиотеки, 3 - удалить кнгу)'))
    if change == 1:
        add_book(file_path)
    elif change == 2:
        print_library(file_path)
    elif change == 3:
        delete_book(file_path)
    #выход из главного цикла или не выход
    change1 = int(input('вы хотите еще что то сделать(1 - да, 2 - нет): '))
    if change1 == 1:
        continue
    else:
        break

#найти механизм взаимодействия с json файлами и реализовать его, назвать переменные нормально