def checkStraightLine(coordinates):
        def slope(fst,scd):
            import sys
            if (scd[0]-fst[0]) == 0:
                return sys.maxsize
            print ("slope = ",(scd[1]-fst[1])/(scd[0]-fst[0]))

            return (scd[1]-fst[1])/(scd[0]-fst[0])
        if len(coordinates) <= 2:
            return True
        fst = coordinates[0]
        scd = coordinates[1]
        m  = slope(fst,scd) 
        print ("m = ", m )
        for i in range(2,len(coordinates)):
            if slope(fst,coordinates[i]) != m:
                return False
        return True
print(checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))