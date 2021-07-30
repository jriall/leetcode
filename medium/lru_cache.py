# LRU Cache

# Design a data structure that follows the constraints of a Least Recently Used
# (LRU) cache.
#
# Implement the LRUCache class:
#
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
#
# int get(int key) Return the value of the key if the key exists, otherwise
# return -1.
# 
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds
# the capacity from this operation, evict the least recently used key.
# 
# The functions get and put must each run in O(1) average time complexity.

class LRUCache:
  
  def __init__(self, capacity: int):
    self.cache_hashtable = {}
    self.cache_dll = DoublyLinkedList()
    self.capacity = capacity
    self.cache_size = 0

  def get(self, key: int) -> int:
    if key in self.cache_hashtable:
      self.cache_dll.set_head(self.cache_hashtable[key])
      return self.cache_hashtable[key].value
    else:
      return -1

  def put(self, key: int, value: int) -> None:
    if key in self.cache_hashtable:
      self.cache_hashtable[key].value = value
    else:
      if self.cache_size < self.capacity:
        self.cache_size += 1
      else:
        tail_key = self.cache_dll.tail.key
        self.cache_dll.evict_tail()
        del self.cache_hashtable[tail_key]
      self.cache_hashtable[key] = LinkedListNode(key, value)
    self.cache_dll.set_head(self.cache_hashtable[key])
    
    
    
class LinkedListNode:
  def __init__(self,
         key: int,
         value: int,
         prev: Optional['LinkedListNode'] = None,
         next: Optional['LinkedListNode'] = None):
    self.key = key
    self.value = value
    self.prev = prev
    self.next = prev
    
  def remove_bindings(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev
    self.prev = None
    self.next = None
  
    
class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    
  def set_head(self, node: 'LinkedListNode'):
    if self.head == node:
      return
    elif self.head is None:
      self.head = node
      self.tail = node
    elif self.head == self.tail:
      self.head.prev = node
      node.next = self.head
      self.head = node
    else:
      if self.tail == node:
        self.evict_tail()
      node.remove_bindings()
      node.next = self.head
      self.head.prev = node
      self.head = node
  
  def evict_tail(self):
    if self.tail == self.head:
      self.head = None
      self.tail = None
      return
    self.tail = self.tail.prev
    self.tail.next = None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)