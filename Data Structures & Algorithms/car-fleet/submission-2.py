# arrange position in ascending order and calculate time taken to reach target for all. (target-position/speed)  and add to stack. now start popping from stack . pop 1 element and then comapre withh top if stack top<=current element just pop from stack and keep comparing with next top. if > then increment feelt counter and update current to top.

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pp = []
        for i,val in enumerate(position):
            pp.append((val,i))
        pp.sort()
        st = []
        for p in pp:
            st.append((target-p[0])/speed[p[1]])
        fleet=1
        cur = st.pop()
        while st:
            if st[-1]<=cur:
                st.pop()
            else:
                cur=st.pop()
                fleet+=1
        return fleet
        