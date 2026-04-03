class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def add_to_head(self, newNode: Node):
        nextNode = self.head.next
        self.head.next = newNode
        newNode.prev = self.head
        newNode.next = nextNode
        nextNode.prev = newNode
    
    def remove_Node(self, removeNode: Node):
        removeNodePrev = removeNode.prev
        removeNodeNext = removeNode.next
        removeNodePrev.next = removeNodeNext
        removeNodeNext.prev = removeNodePrev

    def get(self, key: int) -> int:
        if key in self.cache:
            getNode = self.cache[key]
            self.remove_Node(getNode)
            self.add_to_head(getNode)
            return getNode.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            updateNode = self.cache[key]
            updateNode.val = value
            self.remove_Node(updateNode)
            self.add_to_head(updateNode)
            return
        
        if self.capacity == len(self.cache):
            # make space by eviting
            removeNode = self.tail.prev
            self.cache.pop(removeNode.key)
            self.remove_Node(removeNode)
        
        # add new node
        newNode = Node(key, value)
        self.cache[key] = newNode
        self.add_to_head(newNode)

        

        
