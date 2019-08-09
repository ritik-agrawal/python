class Node:
    def __init__(self, data):
        self.__data=data
        self.__next=None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data=data

    def get_next(self):
        return self.__next

    def set_next(self, node):
        self.__next=node

class que:
    def __init__(self):
        self.__front=None
        self.__rear=None

    def get_front(self):
        return self.__front

    def set_front(self,node):
        self.__front=node

    def get_rear(self):
        return self.__rear

    def set_rear(self, node):
        self.__rear=node

    def display(self):
        temp=self.get_front()
        while temp is not None:
            print(temp.get_data())
            temp=temp.get_next()

    def isempty(self):
        front=self.get_front()
        rear=self.get_rear()
        if front is None and rear is None:
            return True
        else:
            return False

    def enque(self, element):
        node=Node(element)
        rear=self.get_rear()
        if self.isempty():
            self.set_front(node)
            self.set_rear(node)
        else:
            rear.set_next(node)
            self.set_rear(node)

    def deque(self):
        front=self.get_front()
        if self.isempty():
            print("Given Queue is empty")
        else:
            print("Dequeued:{}".format(front.get_data()))
            if front.get_next() is None:
                self.__front=self.__rear=None
                self.isempty()
            else:
                self.set_front(front.get_next())

q_list=que()
q_list.enque("Rk")
q_list.enque(1)
q_list.enque("sj")
q_list.enque(8)
q_list.display()
q_list.deque()
q_list.display()
q_list.deque()
q_list.display()
q_list.deque()
q_list.display()
q_list.deque()
q_list.display()
q_list.deque()
