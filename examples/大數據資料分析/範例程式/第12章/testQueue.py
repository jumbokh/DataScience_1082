from queueClass import Queue

queueObj = Queue()
for i in range(1, 6):
    queueObj.insert(i)

while not queueObj.isEmpty():
    print(queueObj.delete(), end = ' ')