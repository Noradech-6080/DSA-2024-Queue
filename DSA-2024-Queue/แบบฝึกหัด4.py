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


class BankCustomer:
    def __init__(self, name, transaction_type):
        self.name = name
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.name} (ธุรกรรม: {self.transaction_type})"


class BankQueueSystem:
    def __init__(self):
        self.waiting_queue = Queue()

    def add_customer(self, name, transaction_type):
        customer = BankCustomer(name, transaction_type)
        self.waiting_queue.enqueue(customer)
        print(f"ลูกค้า {name} (ธุรกรรม: {transaction_type}) เข้าคิวที่ {self.waiting_queue.size()}")

    def serve_customer(self):
        if not self.waiting_queue.is_empty():
            customer = self.waiting_queue.dequeue()
            print(f"กำลังเสิร์ฟลูกค้า: {customer}")
        else:
            print("ไม่มีลูกค้าในคิว")

    def show_queue(self):
        if self.waiting_queue.is_empty():
            print("ไม่มีลูกค้าในคิว")
        else:
            print("คิวปัจจุบัน:")
            for idx, customer in enumerate(self.waiting_queue.items, 1):
                print(f"{idx}. {customer}")
        print(f"จำนวนลูกค้าในคิว: {self.waiting_queue.size()}")

    def estimate_wait_time(self):
        wait_time_per_person = 5  #นาที
        queue_size = self.waiting_queue.size()
        if queue_size > 0:
            total_wait_time = queue_size * wait_time_per_person
            print(f"ประมาณการเวลารอ: {total_wait_time} นาที")
        else:
            print("ไม่มีลูกค้าในคิว")

bank_queue = BankQueueSystem()

bank_queue.add_customer("ลูกค้า 1", "ฝากเงิน") #เพิ่มลูกค้า
bank_queue.add_customer("ลูกค้า 2", "ถอนเงิน")
bank_queue.add_customer("ลูกค้า 3", "ชำระบิล")

bank_queue.show_queue() #แสดงคิว

bank_queue.estimate_wait_time() #แสดงเวลารอ

bank_queue.serve_customer() #เสิร์ฟลูกค้า

bank_queue.show_queue() #แสดงคิวหลังเสิร์ฟลูกค้า

bank_queue.estimate_wait_time() #แสดงเวลารอหลังเสิร์ฟ