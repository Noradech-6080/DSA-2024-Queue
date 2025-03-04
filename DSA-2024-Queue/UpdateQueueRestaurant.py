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
        return None  #เพิ่มการคืนค่าNone ถ้าคิวว่าง

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()

    def peek_last(self):
        if not self.is_empty():
            return self.items[-1]
        return None

class Restaurant:
    def __init__(self):
        self.waiting_queue = Queue()

    def add_customer(self, name):
        self.waiting_queue.enqueue(name)
        print(f"ลูกค้า {name} เข้าคิวที่ {self.waiting_queue.size()}")

    def serve_customer(self):
        if not self.waiting_queue.is_empty():
            customer = self.waiting_queue.dequeue()
            print(f"กำลังเสิร์ฟลูกค้า: {customer}")
        else:
            print("ไม่มีลูกค้าในคิว")

    def show_queue(self):
        print(f"คิวปัจจุบัน: {self.waiting_queue.items}")
        print(f"จำนวนลูกค้าในคิว: {self.waiting_queue.size()}")

restaurant = Restaurant()

restaurant.add_customer("ลูกค้า 1") #เพิ่มลูกค้า
restaurant.add_customer("ลูกค้า 2")

restaurant.show_queue() #แสดงคิว

restaurant.serve_customer() #เสิร์ฟลูกค้า

restaurant.show_queue()

restaurant.serve_customer()

restaurant.serve_customer()  #เสิร์ฟลูกค้าเมื่อคิวว่าง