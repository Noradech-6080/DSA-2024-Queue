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

    def clear(self):
        self.items.clear()

    def peek_last(self):
        if not self.is_empty():
            return self.items[-1]
        return None


class Customer:
    def __init__(self, name, service_type):
        self.name = name
        self.service_type = service_type

    def __str__(self):
        return f"{self.name} (บริการ: {self.service_type})"


class HaircutQueueSystem:
    def __init__(self):
        self.waiting_queue = Queue()
        #เวลาที่ใช้สำหรับแต่ละบริการ(นาที)
        self.service_times = {
            "ตัดผม": 30,
            "สระ": 20,
            "ย้อมสี": 60
        }

    def add_customer(self, name, service_type):
        if service_type not in self.service_times:
            print("บริการไม่ถูกต้อง กรุณาเลือกจาก 'ตัดผม', 'สระ', หรือ 'ย้อมสี'")
            return
        customer = Customer(name, service_type)
        self.waiting_queue.enqueue(customer)
        print(f"ลูกค้า {name} (บริการ: {service_type}) เข้าคิวที่ {self.waiting_queue.size()}")

    def show_queue(self):
        if self.waiting_queue.is_empty():
            print("ไม่มีลูกค้าในคิว")
        else:
            print("คิวปัจจุบัน:")
            for idx, customer in enumerate(self.waiting_queue.items, 1):
                print(f"{idx}. {customer}")
        print(f"จำนวนลูกค้าในคิว: {self.waiting_queue.size()}")

    def serve_customer(self):
        if not self.waiting_queue.is_empty():
            customer = self.waiting_queue.dequeue()
            wait_time = self.service_times[customer.service_type]
            print(f"กำลังเสิร์ฟลูกค้า: {customer}")
            print(f"เวลาที่ใช้บริการ: {wait_time} นาที")
        else:
            print("ไม่มีลูกค้าในคิว")

    def estimate_wait_time(self):
        total_wait_time = 0
        for customer in self.waiting_queue.items:
            total_wait_time += self.service_times[customer.service_type]
        print(f"ประมาณการเวลารอทั้งหมด: {total_wait_time} นาที")

haircut_queue = HaircutQueueSystem()

haircut_queue.add_customer("ลูกค้า 1", "ตัดผม") #เพิ่มลูกค้า
haircut_queue.add_customer("ลูกค้า 2", "สระ")
haircut_queue.add_customer("ลูกค้า 3", "ย้อมสี")

haircut_queue.show_queue()

haircut_queue.estimate_wait_time() #แสดงเวลารอ

haircut_queue.serve_customer() #เสิร์ฟลูกค้า

haircut_queue.show_queue() #แสดงคิวหลังเสิร์ฟลูกค้า

haircut_queue.estimate_wait_time() #แสดงเวลารอหลังเสิร์ฟ
