class Node:
  def __init__(self, key):
    self.key = key
    self.prev = None
    self.next = None

class LRUCache:
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.cache = {}
    self.queryHead = Node(None)
    self.queryTail = Node(None)
    self.queryHead.next = self.queryTail
    self.queryTail.prev = self.queryHead

  def addKeyToQuery(self, key):
    if key in self.cache:
      node = self.cache[key]
      node.prev.next = node.next
      node.next.prev = node.prev
    else:
      if len(self.cache) >= self.capacity:
        lru = self.queryTail.prev
        lru.prev.next = self.queryTail
        self.queryTail.prev = lru.prev
        del self.cache[lru.key]

      node = Node(key)
      self.cache[key] = node

    node.next = self.queryHead.next
    node.prev = self.queryHead
    self.queryHead.next.prev = node
    self.queryHead.next = node

  def put(self, key, value):
    self.addKeyToQuery(key)
    self.cache[key].value = value

  def get(self, key):
    if key in self.cache:
      self.addKeyToQuery(key)
      return self.cache[key].value
    return -1



cache = LRUCache(2)