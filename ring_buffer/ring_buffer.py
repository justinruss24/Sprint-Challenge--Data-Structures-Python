class RingBuffer:
    def __init__(self, capacity):
        self.storage = []
        self.capacity = capacity
        self.num_items = 0
        self.oldest = None

    def append(self, item):
        if self.storage:
            if self.num_items < self.capacity:
                self.storage.append(item)
                self.num_items += 1
            else:
                self.storage[self.oldest] = item
                self.oldest += 1
                if self.oldest >= self.capacity:
                    self.oldest = 0
        else:
            self.storage.append(item)
            self.oldest = 0
            self.num_items = 1

    def get(self):
        return self.storage