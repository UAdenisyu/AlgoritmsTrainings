import unittest
from LRU_cache import LRUCache

class TestLRUCache(unittest.TestCase):
    def test_put_and_get(self):
        cache = LRUCache(2)
        cache.put(1, 10)
        self.assertEqual(cache.get(1), 10, "Should return 10")

    def test_eviction(self):
        cache = LRUCache(2)
        cache.put(1, 10)
        cache.put(2, 20)
        cache.put(3, 30)  # Key 1 should be evicted
        self.assertEqual(cache.get(1), -1, "Should return -1 for evicted key")
        self.assertEqual(cache.get(2), 20, "Should return 20")
        self.assertEqual(cache.get(3), 30, "Should return 30")

    def test_update_existing_key(self):
        cache = LRUCache(2)
        cache.put(1, 10)
        cache.put(1, 15)
        self.assertEqual(cache.get(1), 15, "Should return updated value 15")

    def test_ordering(self):
        cache = LRUCache(2)
        cache.put(1, 10)
        cache.put(2, 20)
        cache.get(1)  # Access key 1 to make it most recently used
        cache.put(3, 30)  # Key 2 should be evicted
        self.assertEqual(cache.get(2), -1, "Should return -1 for evicted key")
        self.assertEqual(cache.get(1), 10, "Should return 10")
        self.assertEqual(cache.get(3), 30, "Should return 30")

if __name__ == "__main__":
    unittest.main()