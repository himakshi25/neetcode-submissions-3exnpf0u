class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        res = [0]*l
        stack = [0]
        for i in range(1,l):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                t=stack[-1]
                res[t] = i-t
                stack.pop()
            stack.append(i)
        return res




        
            
        