# Hasmap/Dictionary and Double Linked List approach

# Base class
class LRUCache(object):
  def __init__(self, capacity):
      self.capacity = capacity
      self.list = DoubleLinkedList()
      self.nodes = {}

  def put(self, key, value):
    # Get the node for given key, else return None
    node = self.nodes.get(key, None)

    # If the key is in the hashmap/dictionary, update the value
    # and move it to the front of the list
    if node != None:
      node.data.value = value
      self.list.move_to_front(node)
      return

    # If the cache is at capacity, remove the least recently used key
    if self.list.capacity == self.capacity:
      lru = self.list.remove_tail()
      del self.nodes[lru.data.key]
    
    self.nodes[key] = self.list.unshift(KVPair(key, value))
  
  def get(self, key):
    node = self.nodes.get(key, None)

    # If the key doesn't exist, return none
    if node is None:
      return -1
    
    # Move the node to the front of the list, since it is being accessed
    self.list.move_to_front(node)
    return node.data.value

# Helper classes
class KVPair(object):
  def __init__(self, key, value):
    self.key = key
    self.value = value

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class DoubleLinkedList(object):
  def __init__(self):
    self.root = Node(None)
    self.capacity = 0

    # The root node should point to itself when the list is empty
    self.root.next = self.root
    self.root.prev = self.root

  def move_to_front(self, node):
    # Guard against empty nodes
    if node is None:
      return None
    elif node.prev is not None and node.next is not None:
      self.isolate(node)

    # Change the node position so that it points to root as its previous
    # and points to the old head node as its next
    node.prev = self.root
    node.next = self.root.next

    # Change the old head node's prev reference to point to our new node (moves down the circular list)
    # and point the root's next pointer to our new node (inserts our node to the front)
    self.root.next.prev = node
    self.root.next = node
    return node
  
  def unshift(self, data):
    node = Node(data)
    self.move_to_front(node)
    self.capacity += 1
    return node

  @staticmethod
  def isolate(node):
    # Remove the node from its current position
    # by linking the next node to the previous node in the list
    # and the previous node to the next node in the list

    # Visulizations: https://miro.medium.com/max/1300/1*myztJG4u2y5oau8_JcPe4w.png, https://miro.medium.com/max/1400/0*46btArIaub0qpvcD.gif
    node.next.prev = node.prev
    node.prev.next = node.next

    # Remove the references of prev and next from the node (isolating it)
    node.next = None
    node.prev = None 
    return node

  def remove_tail(self):
    # If the list is empty, no need to remove the tail
    if self.capacity == 0:
      return None
    
    # Grab the reference to the roots previous node (the last node in the circular list)
    removed = self.isolate(self.root.prev)
    self.capacity -= 1
    return removed


# Execute test
# Input: ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"][ ([2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]) ];
# Expected output: [null,null,null,1,null,-1,null,-1,3,4]
lru_cache = LRUCache(2)
results_list = {
  lru_cache.put(1, 1),  # cache is {1=1}
  lru_cache.put(2, 2),  # cache is {1=1, 2=2}
  lru_cache.get(1),     # return 1
  lru_cache.put(3, 3),  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
  lru_cache.get(2),     # returns -1 (not found)
  lru_cache.put(4, 4),  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
  lru_cache.get(1),     # return -1 (not found)
  lru_cache.get(3),     # return 3
  lru_cache.get(4),     # return 4
}
print(results_list)