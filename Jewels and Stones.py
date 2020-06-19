class Solution:
    def numJewelsInStones(self, J, S):
        if len(J) == 0 or len(S) == 0:
            return 0 
        sum = 0
        d = dict()
        for c in S :
            if c in d:
                d[c]+=1
            else :
                d[c]=1
        for c in J :
            if c in d :
                sum += d[c]

        return sum
J = "aA"
S = "aAAbbbb"
s = Solution()
print(s.numJewelsInStones(J,S))