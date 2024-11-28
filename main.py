class MyClass:
    """
    Описание класса MyClass
    """
    def __init__(self, name):
        """
         инициализаия класса
        """
        self.name = name

    def say_hello(self):
        """
        Метод для приветствия
        """
        print(f"Привет {self.name}")