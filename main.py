from dataclasses import dataclass


#создаем класс Node, который представляет узел в двусвязном списке. Узел содержит ключ, указатель на следующий узел и указатель на предыдущий узел.

@dataclass
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None

#создаем класс LinkedList, который представляет сам список
class LinkedList:

#создается класс LinkedList, который представляет сам список
    def __init__(self):
        self.head = None

    #функция для вставки нового узла начало списка
    def insert_at_head(self, key):
        new_node = Node(key)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        
#функция для печати списка
    def print_list(self):
        current = self.head
        while current is not None:
            print(current.key)
            current = current.next


#создается экземпляр класса LinkedList, добавляются несколько узлов с ключами, для примера взял числа(3, 11 и 7), и затем вызывается метод print_list для печати содержимого списка.
linked_list = LinkedList()
linked_list.insert_at_head(3)
linked_list.insert_at_head(11)
linked_list.insert_at_head(7)
linked_list.print_list()
