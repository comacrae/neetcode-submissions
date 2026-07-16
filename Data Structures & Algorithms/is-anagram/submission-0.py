class Solution:
    def addToDict(self, ltr:str, ltr_dict: dict) -> dict:
        if ltr in ltr_dict:
            ltr_dict[ltr] += 1
        else:
            ltr_dict[ltr] = 1
        return ltr_dict
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for idx in range(0,len(s)):
            s_ltr = s[idx]
            t_ltr = t[idx]
            self.addToDict(s_ltr, s_dict)
            self.addToDict(t_ltr, t_dict)
            
        if s_dict.keys() != t_dict.keys():
            return False
        
        for k in s_dict.keys():
            if s_dict[k] != t_dict[k]:
                return False
        return True
        
