def intervalIntersection(A, B):
    out = []
    i=0
    j=0
    while(i < len(A) and j < len(B)):
        new = [max(A[i][0],B[j][0]),min(A[i][1],B[j][1])]
        if (new[0]<=new[1]):
            out.append(new)
        if (A[i][1] > B[j][1]):
            j += 1
        elif(A[i][1] < B[j][1]):
            i += 1
        else :
            i+=1 
            j+=1
    
    return out

A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]      
print(intervalIntersection(A,B))