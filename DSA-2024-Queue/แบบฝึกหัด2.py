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

    #เมธอดclear() ที่จะล้างข้อมูลในคิว
    def clear(self):
        self.items.clear()

    #เมธอดpeek_last() เพื่อดูข้อมูลตัวสุดท้ายโดยไม่นำออก
    def peek_last(self):
        if not self.is_empty():
            return self.items[-1]  #คืนค่าข้อมูลตัวสุดท้าย
        return None
    
queue = Queue()

queue.enqueue(12) #เพิ่มข้อมูล
queue.enqueue(22)
queue.enqueue(26)

print("ข้อมูลตัวสุดท้ายในคิว:", queue.peek_last())  #แสดงข้อมูลตัวสุดท้าย

queue.dequeue()

print("ข้อมูลตัวสุดท้ายในคิวหลัง dequeue:", queue.peek_last())  #แสดงข้อมูลตัวสุดท้ายในคิวหลังจากdequeue
