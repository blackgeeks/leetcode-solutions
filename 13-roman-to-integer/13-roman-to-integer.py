class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = 0
        for i in range(0, len(s)-1):
            if ((s[i] == 'I' and s[i+1] in ['V', 'X']) or 
               (s[i] == 'X' and s[i+1] in ['L', 'C']) or
               (s[i] == 'C' and s[i+1] in ['D', 'M'])):
                num -= nums[s[i]]

            else:
                num += nums[s[i]]
            
        return num + nums[s[-1]]