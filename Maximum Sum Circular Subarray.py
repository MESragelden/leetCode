def maxSubarraySumCircular(A):
    import sys
    maximum = A[0] 
    last = A[0]
    summation = sum(A)
    print ("Summation = ",summation)
    for ele in A[1:] :
        maximum = max(maximum + ele,maximum)
        last = ele
    print (last ,maximum)



maxSubarraySumCircular([1,-9,1,2,3,4,5,6,7,8,9,-9,1])
        