
class DeQueue:
    class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def enqueue_head(self, data) -> bool:
        """
        Добавляет элемент в очередь c головы
        :return: bool
        """
        node = DeQueue.Node(data)

        self.__count += 1

        if self.__count == 1:
            self.__head = node
            self.__tail = node
            return True

        node.prev = self.__head
        self.__head = node

        return True

    def enqueue_tail(self, data) -> bool:
        """
        Добавляет элемент в очередь c хвоста
        :return: bool
        """
        node = DeQueue.Node(data)

        self.__count += 1

        if self.__count == 1:
            self.__head = node
            self.__tail = node
            return True

        self.__tail.prev = node
        self.__tail = node

        return True

    def dequeue_head(self) -> Node or Exception:
        """
        Удаляет элемент из головы очереди и возвращает его
        :return: Возвращает удаленный элемент
        """
        assert self.__count != 0, ValueError('Очередь пуста, удалять нечего')

        result_data = self.__head.data

        self.__head = self.__head.prev

        if self.__count == 1:
            self.__tail = None

        self.__count -= 1

        return result_data

    def dequeue_tail(self) -> Node or Exception:
        """
        Удаляет элемент с хвоста очереди и возвращает его
        :return: Возвращает удаленный элемент
        """
        assert self.__count != 0, ValueError('Очередь пуста, удалять нечего')

        result_data = self.__tail.data

        if self.__count == 1:
            self.dequeue_head()

        iterator = self.__head

        while iterator.prev != self.__tail:
            iterator = iterator.prev

        self.__tail = iterator

        self.__count -= 1

        return result_data

    def __peek_head(self) -> Node:
        """
        :return: Возвращает первый элемент с головы
        """
        return self.__head.data

    def __peek_tail(self) -> Node:
        """
        :return: Возвращает первый элемент с головы
        """
        return self.__tail.data

    def __get_count(self) -> int:
        """
        :return: Возвращает текущее количество элементов в очереди
        """
        return self.__count

    def __is_empty(self) -> bool:
        """
        :return: Возвращает True если очередь пуста и False если в ней есть элементы
        """
        return True if self.__count == 0 else False

    head = property(__peek_head)
    tail = property(__peek_tail)
    count = property(__get_count)
    empty = property(__is_empty)

