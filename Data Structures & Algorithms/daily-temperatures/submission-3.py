class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []

        for i,val in enumerate(temperatures):
            while st and st[-1][0]<val:
                tp = st.pop()
                temperatures[tp[1]]= i-tp[1]
            st.append((val,i))
        
        while st:
            tp = st.pop()
            temperatures[tp[1]]= 0
        return temperatures
        