class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        st=[]
        i=0

        while i<len(asteroids):
            if asteroids[i]<0:
                if st and st[-1]>0:
                    while st and st[-1]>0 and st[-1]<-1*asteroids[i]:
                        st.pop()
                    if st and st[-1] == -1*asteroids[i]:
                        st.pop()
                    elif not st or st[-1]<0:
                        st.append(asteroids[i])
                    i+=1
                else:
                    st.append(asteroids[i])
                    i+=1
            else:
                st.append(asteroids[i])
                i+=1
        return st