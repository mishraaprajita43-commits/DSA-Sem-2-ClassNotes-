class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(item, "inserted into queue")

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            removed = self.queue.pop(0)
            print(removed, "removed from queue")

    def peek(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Front element:", self.queue[0])

    def display(self):
        print("Queue:", self.queue)


q = Queue()

q.enqueue("Aprajita")
q.enqueue("Ritika")
q.enqueue("KALU KALIYA")

q.display()

q.dequeue()

q.display()
q.dequeue()
q.display()
q.dequeue()
q.display()
q.dequeue()
q.display()

#q.peek()