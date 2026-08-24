class ListNode:
    def __init__(self, key=-1, val=0, prev=None, next=None):
        self.val=val
        self.next=next
        self.prev=prev
        self.key=key

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm = {}
        self.ls = ListNode()
        self.head=self.ls
        self.ls_size=0
    

    def push(self, node: ListNode):
        if node is not self.ls:
            print(self.ls.val)
            self.ls.next=node
            node.prev=self.ls
            node.next = None
            self.ls=self.ls.next
    
    def pop(self):
        node = self.head.next
        self.head.next=node.next
        if node.next:
            node.next.prev=self.head
        del self.hm[node.key]
    
    def delete(self, node):
        if node is not self.ls:
            node.prev.next=node.next
            node.next.prev=node.prev

    def get(self, key: int) -> int:
        if key not in self.hm:
            return -1
        node=self.hm[key]
        self.delete(node)
        self.push(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            node=self.hm[key]
            node.val=value
            self.delete(node)
            self.push(node)
            return
        if self.capacity == self.ls_size:
            self.pop()
            self.ls_size-=1
        node=ListNode(key, value)
        self.push(node)
        self.hm[key]=node
        self.ls_size+=1
        
        
