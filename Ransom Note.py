class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran = dict()
        for c in ransomNote:
            if c in ran :
                ran[c]+=1
            else :
                ran[c] = 1
        mag = dict()
        for c in magazine:
            if c in mag:
                mag[c]+=1
            else :
                mag[c]=1
        for ele in ran.keys():
            if ele not in mag :
                return False 
            else :
                if  mag[ele] < ran[ele]:
                    return False
        return True
s = Solution()
print(s.canConstruct("bg","efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"))