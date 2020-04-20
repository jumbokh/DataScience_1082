class Queue:
    def __init__(self):
        self.__items = []

    def isEmpty(self):
        return len(self.__items) == 0

    def insert(self, value):
        self.__items.insert(len(self.__items)+1, value)
        print('%d is added in queue.'%(value))

    def delete(self):
        if self.isEmpty():
            return 'The queue is empty.'
        else:
            return self.__items.pop(0)
        
    def getSize(self):
        return len(self.__items)