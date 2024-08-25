
class LinkedList:
    class Node:
        def __init__(self, data: any):
            """
            Формирует фобьект node
            """
            self.data = data  # Данные, которые хранятся в ноде
            self.next = None  # Ссылка на следующую ноду, в начале, когда список пуст и ссылаться ей не на что, она по умолчанию имеет None

    def __init__(self):
        """
        Формирует объект односвязного списка, то есть списка, элементы которого, не лежат в общей памяти массива, а соеденены ссылочной связбю
        """
        self.__count = 0  # Количество элементов в списке
        self.__head = None  # Указатель, указывает на элемент, находящийся в начале списке, то есть его голово

    def add_back(self, item: any) -> bool or Exception:  # O(1) / O(N) /O(N)
        """
        Добавляет ноду в конец списка
        :param item: Пренимает элемент
        :return: bool or Exception
        """
        node = LinkedList.Node(item)  # Создаем ноду

        self.__count += 1  # Количество нод в списке увеличиваем на 1, потому что так или иначе новая нода добавится

        if self.__count == 1:  # Проверяем: если количество нод в списке = 1, то присваиваем голове списка, которая по умолчанию равна None, первую ноду и тем самым даем __head доступ к полям ноды то есть теперь через __head мы можем к ним обращаться, а именно data и next, затем выходим из функции
            self.__head = node  # __head присваиваем ссылку на новую ноду
            return

        iterator = self.__head  # Если добавляем не первую ноду и self.__head мы не можем двигать потому что ссылка на первую ноду пропадет и нода исчезнет
                                # Поэтому внедряем новую переменную iterator, которой присваиваем self.__head чтобы при ее помощи мы могли перемещаться по ссылкам next которые ссылаются на следующие ноды
                                # То есть iterator теперь как и __head имеет доступ к полям ноды, а именно data и next

        while not (iterator.next is None):  # В цикле обходим все ссылки next до тех пор пока одна из них не будет ссылаться на None
            iterator = iterator.next  # При каждой итерации текущему итератору присваиваем значение ссылки последующего

        iterator.next = node  # Как только мы нашли ссылку, которая ссылается на None то присваиваем ей новую ноду таким образом образуем связь между предыдущей нодой, котоая была последней и новой нодой, которая стала последней

    def add_front(self, item: any) -> bool or Exception:
        """
        Добавляет ноду в начало списка
        :param item: Пренимает элемент
        :return: bool or Exception
        """
        node = LinkedList.Node(item)  # Создаем ноду

        self.__count += 1  # Количество нод в списке увееличиваем на 1, потому что так или иначе новая нодадобавится

        if self.__count == 1:
            self.__head = node  # __head присваиваем ссылку на новую ноду
            return True

        node.next = self.__head  # Берем ссылку новой ноды, которую нам нужно поставить на 1 позицию и присваиваем ей __head, а так как __head содержит ссылку на предыдущую ноду, которая была первой, то получается мы новой ноде присвоили предыдущую первую

        self.__head = node  # Затем мы хеду присваиваем новую ноду, теперь она первая в списке

        return True

    def insert_of_position(self, item: any, position: int) -> bool or Exception:
        """
        Добавляет ноду на определенную позицию
        :param position: Пренимает position, на который нужно добавить ноду
        :return: bool or Exception
        """
        node = LinkedList.Node(item)

        self.__count += 1  # Количество нод в списке увееличиваем на 1, потому что так или иначе новая нодадобавится

        if self.__count == 1:
            self.add_back(item)  # Если список пуст то нет возможности добавить ноду на определенную позицию, поэтому просто добавляем через add_back
            return True

        count_position = 1 # Объявляем счетчик позиций, который затем в цикле будет сравниваться с, полученной от пользователя, позицией

        if position == 1:
            node.next = self.__head  # Берем ссылку новой ноды, которую нам нужно поставить на 1 позицию и присваиваем ей __head, а так как __head содержит ссылку на предыдущую ноду, которая была первой, то получается мы новой ноде присвоили предыдущую первую
            self.__head = node  # __head присваиваем ссылку на новую ноду
            return True

        iterator = self.__head  # Создаем итератор и присваиваем ему значение головы, то есть первую ноду
        iterator_prev = None  # Создаем итератор прев и присваиваем ему значение None

        while count_position != position and not (iterator.next is None): # Цикл продолжает работу пока счетчик позиций не равен, полученной от пользователя, позиции
            iterator_prev = iterator  # Присваиваем iterator_prev значение iterator, то есть сейчас они оба ссылаются на первую ноду
            iterator = iterator.next  # iterator присваиваем значение следующей ноды по ссылке next

            count_position += 1  # Счетчик позиций каждую итерацию увеличивается на 1

            if count_position == position:  # Если счетчик позиций равен переданной позиции то заходим в тело условия
                node.next = iterator  # Ссылке новой ноды присваиваем значение итератора, который в данный момент ссылается на следующую ноду
                iterator_prev.next = node  # Ссылке iterator_prev присваиваем новую ноду, таким образом новая нода внедряется ммежду 2 старых, путем переброса ссылок

                return True
        return False

    def remove_first_node(self) -> Node or Exception:
        """
        Удаляет первую ноду в списке
        :return: Возвращает первую ноду списка или Exception
        """
        assert self.__count != 0, ValueError('В списке отсутствуют элементы, удалять нечего')

        result_data = self.__head.data  # Для того чтобы вернуть удаленную ноду нам нужно ее сохранить в переменную, поскольку ссылок на удаленную ноду больше не будет

        self.__head = self.__head.next  # Обращаемся к голове, которая ссылается на текущую первую ноду и присваиваем ей ссылку этой ноды, а т. к. она ссылается на следующую по счету, то фактически мы первой ноде присваиваем вторую, на первую ноду ссылок больше нет и она удаляется

        self.__count -= 1  # Уменьшаем количество нод в списке после удаления первой ноды

        return result_data  # Возвращаем удаленную первую ноду, значение которой мы присвоили переменной result_node, в ней она и хранится

    def remove_last_node(self) -> Node or Exception:
        """
        Удаляет последнюю ноду в списке
        :return: Возвращает последнюю ноду списка или Exception
        """
        assert self.__count != 0, ValueError('В списке отсутствуют элементы, удалять нечего')

        iterator = self.__head  # Создаем итератор и присваиваем ему значение головы, то есть первую ноду

        while not (iterator.next is None):  # В цикле обходим все ссылки next до тех пор пока одна из них не будет ссылаться на None
            iterator = iterator.next  # При каждой итерации текущему итератору присваиваем значение ссылки последующего

            if iterator.next == None:  # При каждой итерации цикла проверяем это условие, когда наступает случай при котором ссылка итератора ссылается на None мы заходим в блок кода
                result_data = iterator.data  # Создаем локальную переменную и присваиваем ей значение итератора, чтобы сохранить и затем вернуть удаляемую ноду
                iterator = None

                self.__count -= 1

                return result_data

    def remove_node_for_data(self, data) -> Node or Exception:
        """
        Удаляет ноду, данные которой соответствующую переданным
        :param data:
        :return:
        """
        assert self.__count != 0, ValueError('В списке отсутствуют элементы, удалять нечего')

        if self.__head.data == data: # Голова ссылается на первую ноду и имеет доступ к ее полям, проверяем если data первой нолды равна полученному итему то вызываем функцию удаления первого элемента
            self.remove_first_node()

        iterator = self.__head  # Создаем итератор и присваиваем ему значение головы, то есть первую ноду
        iterator_prev = None  # Создаем итератор прев и присваиваем ему значение None

        while iterator.data != data and not (iterator.next is None):  # Если искомый элемент не в первой ноде то в цикле перебираем ссылки, пока не найдется нода с нужными данными
            iterator_prev = iterator  # Присваиваем iterator_prev значение iterator, то есть сейчас они оба ссылаются на первую ноду
            iterator = iterator.next  # iterator присваиваем значение следующей ноды по ссылке next

            if iterator.data == data:  # Каждую итерацию цикла значения итератов меняются потому, что по ссылкам они переходят к следующим нодам и происходит проверка данных, если данные в ноде совпадают с искомыми
                result_data = iterator.data   # Если полученные данные совпали с данными какой либо ноды то эту ноду присваиваем локальной переменной чтобы сохранить ее и вернуть после удаления
                iterator_prev.next = iterator.next  # То iterator_prev через ссылку next присваивается следующая нода по отношению к iterator, таким образом ссылка на ноду, на которой находится итератор (и данные которой совпали с искомыми) пропадает и нода удаляется

                self.__count -= 1

                return result_data # Возвращаем сохраненную ноду

        return False  # Если полученный данные не были найдены ни в одной ноде то вернем False

    def find(self, item) -> bool:
        """
        Обходит всесь список путем присвоению текущему итератору следующего элемента списка через ссылку next и проверяет совпадают ли хранящиеся в элементах данные с полученными, если совпадают то вернет True если обойдя весь список совпадений не найдется, то вернет False
        :param item: Пренимает данные для поиска
        :return: bool
        """
        assert self.__count != 0, ValueError('Список пуст, искать нечего')

        iterator = self.__head

        while iterator.data != item and not (iterator.next is None):
            iterator = iterator.next

            if iterator.data == item:
                return True

        return False

    def __clear(self):
        """
        Очищает всю структуру данных
        :return:
        """
        self.__head = None

    def __peek(self):
        """
        :return: Возвращает ноду, на которую указывает указатель __head
        """
        return self.__head.data

    def __count(self) -> int:
        """
        Подсчитывает количество нод в Структуре данных
        :return:
        """
        return self.__count

    def __is_empty(self):
        """
        :return:  Возвращает true, если список пуст, иначе false
        """
        return True if self.__count == 0 else False

    head = property(__peek)
    clear = property(__clear)
    count = property(__count)
    empty = property(__is_empty)


