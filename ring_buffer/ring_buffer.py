class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage[self.current] = item
    self.current += 1
    if self.current == self.capacity:
      self.current = 0

  def get(self):
    # return self.storage will always return the entire buffer
    temp = []
    for component in self.storage:
      if component:
        temp.append(component)
    return temp