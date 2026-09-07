class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        temp_dict_s = {}

        for i in s:
            if i not in temp_dict_s:
                temp_dict_s[i] = 1
            else: 
                temp_dict_s[i] += 1

        temp_dict_t = {}

        for j in t:
            if j not in temp_dict_t:
                temp_dict_t[j] = 1
            else: 
                temp_dict_t[j] += 1

        
        for i in set(temp_dict_s) | set(temp_dict_t):
            if temp_dict_s.get(i,0) - temp_dict_t.get(i,0) != 0:
                return False
        return True

                