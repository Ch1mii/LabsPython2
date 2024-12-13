class Table:
    """
    Класс описывает объект "Стол".

    Атрибуты:
        length (float): Длина стола в метрах.
        width (float): Ширина стола в метрах.
        material (str): Материал, из которого сделан стол.
    """

    def __init__(self, length: float, width: float, material: str):
        if length <= 0 or width <= 0:
            raise ValueError("Длина и ширина стола должны быть положительными числами.")
        if not material:
            raise ValueError("Материал не может быть пустой строкой.")

        self.length = length
        self.width = width
        self.material = material

    def area(self) -> float:
        """
        Вычисляет площадь стола.

        Returns:
            float: Площадь стола.

        >>> table = Table(2.0, 1.5, "Дерево")
        >>> table.area()
        3.0
        """
        return self.length * self.width

    def is_square(self) -> bool:
        """
        Проверяет, является ли стол квадратным.

        Returns:
            bool: True, если стол квадратный, иначе False.

        >>> table = Table(2.0, 2.0, "Металл")
        >>> table.is_square()
        True
        """
        return self.length == self.width

    def change_material(self, new_material: str) -> None:
        """
        Изменяет материал стола.

        Args:
            new_material (str): Новый материал для стола.

        Raises:
            ValueError: Если новый материал пустой.

        >>> table = Table(2.0, 1.5, "Дерево")
        >>> table.change_material("Металл")
        >>> table.material
        'Металл'
        """
        if not new_material:
            raise ValueError("Материал не может быть пустым.")
        self.material = new_material


class Tree:
    """
    Класс описывает объект "Дерево".

    Атрибуты:
        species (str): Вид дерева.
        height (float): Высота дерева в метрах.
        age (int): Возраст дерева в годах.
    """

    def __init__(self, species: str, height: float, age: int):
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительной.")
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным.")
        if not species:
            raise ValueError("Вид дерева не может быть пустым.")

        self.species = species
        self.height = height
        self.age = age

    def grow(self, years: int = 1) -> None:
        """
        Увеличивает высоту и возраст дерева на заданное количество лет.

        Args:
            years (int): Количество лет роста дерева. По умолчанию 1 год.

        Raises:
            ValueError: Если количество лет отрицательное.

        >>> tree = Tree("Дуб", 10.0, 50)
        >>> tree.grow(5)
        >>> tree.height
        12.5
        """
        if years < 0:
            raise ValueError("Количество лет роста не может быть отрицательным.")
        self.height += years * 0.5  # Пример: дерево растет на 0.5 м в год
        self.age += years

    def is_mature(self) -> bool:
        """
        Проверяет, является ли дерево зрелым (старше 50 лет).

        Returns:
            bool: True, если дерево зрелое, иначе False.

        >>> tree = Tree("Сосна", 15.0, 55)
        >>> tree.is_mature()
        True
        """
        return self.age > 50

    def describe(self) -> str:
        """
        Возвращает строковое описание дерева.

        Returns:
            str: Описание дерева.

        >>> tree = Tree("Береза", 5.0, 10)
        >>> tree.describe()
        'Береза, высота: 5.0 м, возраст: 10 лет.'
        """
        return f"{self.species}, высота: {self.height} м, возраст: {self.age} лет."


class User:
    """
    Класс описывает объект "Пользователь".

    Атрибуты:
        username (str): Имя пользователя.
        email (str): Электронная почта пользователя.
        age (int): Возраст пользователя.
    """

    def __init__(self, username: str, email: str, age: int):
        if age <= 0:
            raise ValueError("Возраст должен быть положительным числом.")
        if "@" not in email:
            raise ValueError("Некорректный адрес электронной почты.")
        if not username:
            raise ValueError("Имя пользователя не может быть пустым.")

        self.username = username
        self.email = email
        self.age = age

    def send_message(self, message: str, recipient: str) -> str:
        """
        Отправляет сообщение другому пользователю.

        Args:
            message (str): Текст сообщения.
            recipient (str): Имя получателя.

        Returns:
            str: Подтверждение отправки сообщения.

        Raises:
            ValueError: Если сообщение пустое или имя получателя не указано.

        >>> user = User("JohnDoe", "john@example.com", 25)
        >>> user.send_message("Привет!", "Jane")
        'Сообщение отправлено Jane: Привет!'
        """
        if not message:
            raise ValueError("Сообщение не может быть пустым.")
        if not recipient:
            raise ValueError("Получатель должен быть указан.")
        return f"Сообщение отправлено {recipient}: {message}"

    def update_email(self, new_email: str) -> None:
        """
        Обновляет адрес электронной почты пользователя.

        Args:
            new_email (str): Новый адрес электронной почты.

        Raises:
            ValueError: Если новый адрес электронной почты некорректен.

        >>> user = User("JohnDoe", "john@example.com", 25)
        >>> user.update_email("john.doe@example.com")
        >>> user.email
        'john.doe@example.com'
        """
        if "@" not in new_email:
            raise ValueError("Некорректный адрес электронной почты.")
        self.email = new_email

    def is_adult(self) -> bool:
        """
        Проверяет, является ли пользователь совершеннолетним (старше 18 лет).

        Returns:
            bool: True, если пользователь совершеннолетний, иначе False.

        >>> user = User("JaneDoe", "jane@example.com", 20)
        >>> user.is_adult()
        True
        """
        return self.age >= 18
