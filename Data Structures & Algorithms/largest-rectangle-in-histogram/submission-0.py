# for any element, check nearest minimum value to its left and right(using monotonic stack). (rightin-leftin-1)*height
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ll,rl=[0]*len(heights),[0]*len(heights)
        st=[]
        for i,h in enumerate(heights):
            if not st:
                ll[i]=-1
                st.append((h,i))
            else:
                while st and st[-1][0]>=h:
                    st.pop()
                if not st:
                    ll[i]=-1
                else:
                    ll[i]=st[-1][1]
                st.append((h,i))
        st=[]
        i=len(heights)-1
        while i>=0:
            if not st:
                rl[i]=len(heights)
                st.append((heights[i],i))
            else:
                while st and st[-1][0]>=heights[i]:
                    st.pop()
                if not st:
                    rl[i]=len(heights)
                else:
                    rl[i]=st[-1][1]
                st.append((heights[i],i))
            i-=1

        rect=0
        for i,h in enumerate(heights):
            rect=max(rect,h*(rl[i]-ll[i]-1))

        return rect
        