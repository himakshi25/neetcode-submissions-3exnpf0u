# push to stack and keep popping if new ele is > stack top
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        ans= [0] * len(temperatures)
        for i,val in enumerate(temperatures):
            while st and st[-1][0]<val:
                tp = st.pop()
                ans[tp[1]]= i-tp[1]
            st.append((val,i))
    
        return ans
        