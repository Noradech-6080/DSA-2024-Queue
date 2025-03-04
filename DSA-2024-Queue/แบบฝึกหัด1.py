class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def size(self):
        return len(self.items)

    def clear(self): #เมธอดclear() ที่จะล้างข้อมูลทั้งหมดในคิว
        self.items.clear()

queue = Queue()

queue.enqueue(12) #เพิ่มข้อมูลลง
queue.enqueue(22)
queue.enqueue(30)

print("คิวก่อนล้าง:", queue.items)  #แสดงข้อมูล

queue.clear() #ล้างข้อมูลทั้งหมด

print("คิวหลังล้าง:", queue.items)  #แสดงข้อมูลในคิวหลังล้าง