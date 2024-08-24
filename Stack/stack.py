class Node:
    def __init__(self, data):
        """
        Формирует фобьект node
        """
        self.data = data  # Данные, которые хранятся в ноде
        self.prev = None  # Ссылка на предыдущую ноду


class Stack:
    def __init__(self):
        """
        Формирует объект Stack
        """
        self.__count = 0  # Количество элементов в стэке
        self.__top = None  # Указатель, указывает на элемент, находящийся на вершине стэка

    def push(self, data) -> None:
        """
        Добавляет объект node в стэк
        :param data: Пренимает пренимает данные ноды
        :return: None
        """
        node = Node(data)

        if self.__count == 0:
            self.__top = node

        node.prev = self.__top
        self.__top = node
        self.__count += 1

    def pop(self) -> None:
        """
        Удаляет объект node из стек путем переноса указателя __top на предыдущую ноду, то есть ссылка на текущую ноду теряется и указатель __top теперь ссылается на предыдущую
        А так как объект живет пока на него есть хоть одна ссылка, а ссылки на верхний элемент теперь нет, поэтому он удаляется из стэка
        :return: None
        """
        assert self.__count != 0, ValueError('Удлять нечего')

        self.__top = self.__top.prev
        self.__count -= 1

    def peek(self):
        """
        :return: Возвращает ноду, на которую указывает указатель __top
        """
        return self.__top

    def is_empty(self) -> bool:
        """
        :return: Возвращает True если в стеке есть хоть 1 элемент, иначе False
        """
        return True if self.__count == 0 else False

    def __get_count(self):
        """
        :return: Возвращает количество элементов в стеке
        """
        return self.__count

    count = property(__get_count)
    top = property(peek)


