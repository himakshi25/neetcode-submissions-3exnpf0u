class Node:
    def __init__(self, val: int, key: int):
        self.val = val
        self.key = key
        self.p = None
        self.n = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm = dict()
        self.head = Node(-1,-1)
        self.cur = self.head
    
    def restructureDLL(self, rn: Node):
        if self.cur == rn:
            return
        prevrn = rn.p
        rnnext = rn.n
        prevrn.n = rnnext
        if rnnext != None:
            rnnext.p = prevrn

        self.cur.n = rn
        rn.p = self.cur
        rn.n = None
        self.cur = rn
        print(f"head: {self.head.n.key}")

    def get(self, key: int) -> int:
        print(f"get: {key} {self.hm}")
        if key in self.hm:
            value=self.hm[key].val
            print(f"got: {key} {value}")
            self.restructureDLL(self.hm[key])
            return value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        print(f"c: {self.capacity} hm: {self.hm} k:{key}")
        # update in DLL
        if key in self.hm:
            # update value
            rn = self.hm[key]
            rn.val = value
            # remove from DLL and add to end.
            self.restructureDLL(rn)
            return

        if self.capacity == len(self.hm):
            # remove head next from DLL
            evictNode = self.head.n
            print(f"evict: {evictNode.key}")
            self.head.n = evictNode.n
            if self.head.n != None:
                self.head.n.p = self.head
            #remove that key from map
            self.hm.pop(evictNode.key)

        # add to map
        node = Node(value, key)
        self.hm[key] = node
        # add to DLL
        self.cur.n = node
        node.p = self.cur
        self.cur = node

