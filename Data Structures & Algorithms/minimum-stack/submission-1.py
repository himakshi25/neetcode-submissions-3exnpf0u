class MinStack:

    def __init__(self):
        self.stack_list = []
        self.stack_list2 = [float('inf')]

    def push(self, val: int) -> None:
        self.stack_list.append(val)
        self.stack_list2.append(min(val,self.stack_list2[-1]))

    def pop(self) -> None:
        self.stack_list.pop()
        self.stack_list2.pop()
        

    def top(self) -> int:
        return self.stack_list[-1]
        

    def getMin(self) -> int:
        return self.stack_list2[-1]
        
