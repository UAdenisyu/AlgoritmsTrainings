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
    if (self.queryHead.key == None):
      self.queryHead.key = key
      return
    if (self.queryTail.key == None):
      self.queryTail.key = key
      return
    node = self.queryHead
    while (node.next != None):
      if (key == node.key):
        node.next = self.queryHead
        self.queryHead.prev = None
        self.queryHead = node
        node.prev = None


      node = node.next
    

  def put(self, key, value):
    print('start cache', self.cache)
    print('start queryHead', self.queryHead)

    if (len(self.cache.keys()) >= self.capacity):
      self.cache.pop(self.query[0])
    self.cache[key] = value
    print('end cache', self.cache)
    print('end queryHead', self.queryHead)
    return self.cache

  def get(self, key):
    return self.cache[key] if self.cache.get(key) != None else -1



cache = LRUCache(2)

cache.put(1, 1)       # Кеш: {1=1}
cache.put(2, 2)       # Кеш: {1=1, 2=2}
print(cache.get(1))   # Возвращает 1. Кеш: {2=2, 1=1}
cache.put(3, 3)       # Кеш: {1=1, 3=3} (удалён ключ 2)
print(cache.get(2))   # Возвращает -1 (ключ 2 отсутствует)
cache.put(4, 4)       # Кеш: {3=3, 4=4} (удалён ключ 1)
print(cache.get(1))   # Возвращает -1 (ключ 1 отсутствует)
print(cache.get(3))   # Возвращает 3. Кеш: {4=4, 3=3}
print(cache.get(4))   # Возвращает 4. Кеш: {3=3, 4=4}


# queryHead = {
#   "current": None,
#   "prev": None,
# }

