
def malloc(size) -> list or Exception:
    """
    Увеличивает количество ячеек массива, в которые можем добавлять элементы, то есть другими словами увеличивает размер памяти
    :param size: Пренимает количество
    :return: Возвращает Список с ячейками, заполненными None
    """
    assert size > 0, ValueError()

    array = [None] * size

    return array


class DList:
    def __init__(self, size: int):
        self.__count = 0 # Количество фактически добавленных элементов в наш список, отличных от None. В данном примере count = 3 элемента [2, 5, 7, None, None, None, None]
        self.__size = size + (size // 2) # Количество ячеек, созданных в списке, в которые мы кладем элементы, если в ячейке нет элемента то ее заполняет None [2, 5, 7, None, None, None, None] в данном примере size = 7
        self.__array_memory = None  # Сам массив, в который мы добавляем элементы, по умолчанию равен None, то есть ссылка ссылается на пустоту, массива пока что нет, если количество ячеек, созданных в списке = 0

        if self.__size != 0:
            self.__array_memory = malloc(self.__size)

    def __realloc(self) -> None:
        """
        Добавляет в массив ячейки памяти, заполненные None
        :return: None
        """
        self.__size = self.__size + (self.__size // 2)  # ????
        new_array_memory = malloc(self.__size)

        for i in range(0, self.__count, 1):
            new_array_memory[i] = self.__array_memory[i]

        self.__array_memory = new_array_memory

    def add_back(self, item: any) -> bool: # Сложность алгоритма O(1) / O(N)
        """
        Добавляет элемент в конец списка
        :param item: Пренимает итем для добавления
        :return: None
        """
        if self.__count == self.__size:

            self.__realloc()

        self.__array_memory[self.__count] = item
        self.__count += 1

        return True

    def add_front(self, item: any) -> bool or Exception: # Сложность алгоритма O(N)
        """
        Добавляет элемент в начало списка
        :param item: Пренимает итем для добавления
        :return: None
        """
        if self.__count == 0:
            self.add_back(item)
            return True

        if self.__count == self.__size:
            self.__realloc()

        for i in range(self.__count, 0, -1):
            self.__array_memory[i], self.__array_memory[i-1] = self.__array_memory[i-1], self.__array_memory[i]

        self.__array_memory[0] = item

        self.__count += 1

        return True

    def remove_back(self) -> bool or Exception: # Сложность алгоритма O(1)
        """
        Удаляет последний элемент
        :return:
        """
        assert self.__count != 0, ValueError('Список пуст, удалять нечего')

        self.__array_memory[self.__count-1] = None

        return True

    def remove_front(self) -> bool or Exception: # Сложность алгоритма O(1) / O(N)
        """
        Удаляет первый элемент списка
        :return:
        """
        assert self.__count != 0, ValueError('Список пуст, удалять нечего')

        self.__array_memory[0] = None

        if self.__count == 1:
            return True

        for i in range(0, self.__count, 1):
            self.__array_memory[i], self.__array_memory[i+1] = self.__array_memory[i+1], self.__array_memory[i]

            return True

    def remove_of_data(self, data: any) -> bool or Exception: # Сложность алгоритма O(1) / O(N) / O(N)
        """
        Удаляяет первое вхождение элемента item. Если данного элемента в списке нет, породить исключение ValueError()
        :param item: Пренимает элемент поиска
        :return: True или ValueError
        """
        assert data in self.__array_memory, ValueError('В массиве нет такого элемента')

        if self.__count == 1:
            self.remove_front()
            return True

        for i in range(0, self.__count, 1):

            if self.__array_memory[i] == data:
                self.__array_memory[i], self.__array_memory[i+1] = self.__array_memory[i+1], self.__array_memory[i]

        self.__array_memory[self.__count] = None

        self.__count -= 1

        return True

    def remove_of_index(self, index: int) -> bool or Exception: # Сложность алгоритма O(1) / O(N) / O(N)
        """
         Удаляет элемент по индексу. если индекс выходит за допустимые границы, породить исключение ValueError()
        :param index: Пренимает индекс удаляемого элемента
        :return: True или ValueError
        """
        assert index >= 0 and index <= self.__count-1, ValueError('Данный индекс отсутствует в массиве')

        for i in range(index, self.__count, 1):

            self.__array_memory[i], self.__array_memory[i+1] = self.__array_memory[i+1], self.__array_memory[i]

        self.__array_memory[self.__count] = None

        self.__count -= 1

        return True

    def find(self, item: any) -> int: # Сложность алгоритма O(1) / O(N) / O(N)
        """
         Ищет элемент в коллекции
        :param item: Пренимает элемент поиска
        :return: Если элемент найден, вернуть его индекс, иначе -1
        """
        assert item in self.__array_memory, ValueError('В массиве нет такого элемента')

        for i in range(0, self.__count, 1):
            if self.__array_memory[i] == item:
                return i

        return -1

    def insert_to_index(self, item: any, index: int) -> bool or Exception: # Сложность алгоритма O(1) / O(N) / O(N)
        """
        Вставляет элемент item на позицию index (происходит циклический сдвиг вправо)
        :param item: Пренимает элемент
        :param index: Пренимает индекс
        :return: bool
        """
        assert index >= 0 and index <= self.__size, ValueError('Данный индекс отсутствует в массиве')

        if self.__count == 0 or index >= self.__count:
            self.add_back(item)
            return True

        if self.__count == self.__size:
            self.__realloc()

        for i in range(self.__count, index, -1):
            self.__array_memory[i], self.__array_memory[i-1] = self.__array_memory[i-1], self.__array_memory[i]

        self.__array_memory[index] = item
        self.__count += 1

        return True

    def revert(self) -> bool or Exception:
        """
        Выполняет реверс ячеек массива, заполненных элементами
        :return: Возвращает реверсированный массив
        """
        assert self.__count >= 2, ValueError('Реверс массива не возможен если в нем меньше 2 элементов')

        for i in range(0, self.__count // 2, 1):

            self.__array_memory[i], self.__array_memory[self.__count-i-1] = self.__array_memory[self.__count-i-1], self.__array_memory[i]

        return True

    def sort(self, condition=lambda x, y: x < y) -> bool or Exception:
        """
        Выполняет сортировку массива исходя из заданных параметров, которые устанавливает lambda функция
        :param condition: Пренимает lambda функцию
        :return: Возвращает сортированный массив
        """
        assert self.__count >= 2, ValueError('Сортировка массива не возможена если в нем меньше 2 элементов')

        for i in range(0, self.__count, 1):
            index_min = i

            for j in range(i+1, self.__count, 1):
                if condition(self.__array_memory[index_min], self.__array_memory[j]):
                    index_min = j

            self.__array_memory[i], self.__array_memory[index_min] = self.__array_memory[index_min], self.__array_memory[i]

        return True

    def count_item(self, item: any) -> int or Exception:
        """
        Выполняет подсчет количества вхождений, переданного в метод, элемента
        :param item:
        :return:
        """
        assert self.__count > 0, ValueError('Подсчет невозможен, поскольку в массиве нет элементов')

        assert item in self.__array_memory, ValueError('Полученный элемент отсутствует в массиве')

        count_entry = 0

        for i in range(0, self.__count, 1):
            if self.__array_memory[i] == item:
                count_entry += 1

        return count_entry

    def is_empty(self) -> bool: # Сложность алгоритма O(1)
        """
        Проверяет список на пустоту. Если список пустой
        :return: вернуть True, иначе False
        """
        return True if self.__count == 0 else False

    def __get_array_memory(self):
        return self.__array_memory

    def __get_size(self):
        return self.__size

    def __get_count(self):
        return self.__count

    array = property(__get_array_memory)

    count = property(__get_count)

    size = property(__get_size)

