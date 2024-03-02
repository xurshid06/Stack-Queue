# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def empty(self):
#         return len(self.items) == 0
#     def insert(self, index, item):
#         if not self.empty():
#             self.items.insert(index, item)
#         else:
#             print("Stack is empty")
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self, item):
#         if not self.empty():
#             self.items.pop()
#         else:
#             return "Stack is empty"
#     def peek(self):
#         if not self.items:
#             return self.items[-1]
#         else:
#             print("Stack is empty")
#
#     def size(self):
#         if not self.items:
#             return len(self.items)
# stak = Stack()
# stak.push(100)
# stak.push(101)
# stak.push(102)
# stak.push(103)
# stak.push(104)
# stak.insert(0, 99)
# stak.insert(0, 98)
# stak.insert(0, 97)
# a = stak.size()
# print(a)
# print(stak.items)
#

############ Queue

class Queue:
    def __init__(self):
        self.items = []
    def empty(self):
        return len(self.items) == 0
    def insert(self, index, item):
        if not self.empty():
            self.items.insert(index ,item)
        else:
            print("Queue is empty")
    def append(self, item):

        self.items.append(item)
    def pop(self):
        if not self.empty():
            self.items.pop()
        else:
            print("Queue is empty")
    def peek(self):
        if not self.empty():
            return self.items[0]
        else:
            print("Queue is empty")
    def size(self):
        return len(self.items)
    def reversed(self):
        return self.items.reverse()

queue = Queue()
queue.append(200)
queue.append(201)
queue.append(202)
queue.append(203)
queue.append(204)
queue.insert(0, 199)
queue.insert(0, 198)
queue.insert(0, 197)
queue.insert(0, 196)
queue.pop()
queue.peek()
queue.reversed()
print(queue.items)