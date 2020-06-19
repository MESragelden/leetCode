class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust)<N-1:
            return -1
        if (len(trust)==0) and (N == 1) :
            return 1
        arr = [0] * (N+1)
        for i,j in trust:
            arr[i]-=1
            arr[j]+=1
        #return arr
        maxx = max(arr)
        if maxx == N-1:
            return arr.index(maxx)
        else :
            return -1 
