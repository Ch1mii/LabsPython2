BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_, name, pages):
        """
        Конструктор класса Book.
        :param id_: идентификатор книги (целое число)
        :param name: название книги (строка)
        :param pages: количество страниц в книге (целое число)
        """
        self.id = id_  # Используем id_ чтобы избежать конфликтов с встроенной функцией id
        self.name = name
        self.pages = pages

    def __str__(self):
        """
        Метод возвращает строковое представление книги в формате:
        "Книга \"название_книги\""
        """
        return f'Книга "{self.name}"'

    def __repr__(self):
        """
        Метод возвращает строку, позволяющую создать объект идентично.
        Формат: Book(id=..., name=..., pages=...)
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


# Пример использования
if __name__ == "__main__":
    # Инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"])
        for book_dict in [
            {"id_": 1, "name": "test_name_1", "pages": 200},
            {"id_": 2, "name": "test_name_2", "pages": 400},
        ]
    ]

    for book in list_books:
        print(book)  # Проверяем метод __str__

    print(list_books)  # Проверяем метод __repr__
