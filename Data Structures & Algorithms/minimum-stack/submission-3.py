# create 2 stack, one normal one min stack, push to the min-stack if the new value is less than or equal to the current minimum — the equal case matters, because if I only checked strictly less-than, popping a duplicate minimum later would desync the two stacks and I'd lose track of the true minimum still sitting in the main stack.
class MinStack:

    def __init__(self):
        self.st=[]
        self.minst=[]
        

    def push(self, val: int) -> None:
        self.st.append(val)
        if self.minst:
            if val<=self.minst[-1]:
                self.minst.append(val)
        else:
            self.minst.append(val)
        

    def pop(self) -> None:
        ele = self.st.pop()
        if ele == self.minst[-1]:
            self.minst.pop()
        

    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        return self.minst[-1]
        
