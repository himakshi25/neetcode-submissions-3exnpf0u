class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]

        for t in tokens:
            if t in ['+','-','*','/']:
                v1=int(st.pop())
                v2=int(st.pop())
                ans=0
                if t == '+':
                    ans=v2+v1
                elif t == '-':
                    ans=v2-v1
                elif t == '*':
                    ans=v2*v1
                else:
                    ans=int(v2/v1)
                st.append(str(ans))
            else:
                st.append(t)
        return int(st.pop())
        