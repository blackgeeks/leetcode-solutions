class Solution:
    def isValid(self, s: str) -> bool:
        
        # replace all pairs of brackets with ""
        # at the end, if string is empty, its true.

        iteration = len(s)
        
        while iteration!=0 and iteration%2==0:
            s = s.replace("()","")
            s = s.replace("{}","")            
            s = s.replace("[]","")      
            if len(s) < iteration:
                iteration = len(s)
            else:
                iteration = 0

            
        return s==""