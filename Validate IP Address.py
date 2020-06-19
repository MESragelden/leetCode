def validIPAddress(IP):
    def chechIPV4 (l):
        for m in l :
            try:
                if int(m) not in range (0,255):
                    return "Neither"
            except:
                return "Neither"
        return "IPv4"
        
    def valid_ipv6_num(num):
        if not num: return False
        if not set(num).issubset(hexdigits): return False
        return len(num) <= 4
        
    def valid_ipv6(IP):
        for num in IP.split(':'):
            if not valid_ipv6_num(num): return 'Neither'
        return 'IPv6'
    hexdigits = set('0123456789abcdefABCDEF')
    import re    
    l = re.split("[.|:]",IP)
    if len(l)== 4:
        return chechIPV4(l)
    elif len(l) == 8:
        return valid_ipv6(IP)
    else : 
        return "Neither"


Input1 = "172.16.254.1"
Output1 = "IPv4"
print (validIPAddress(Input1) == Output1)

Input2 = "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output2 = "IPv6"
print (validIPAddress(Input2) == Output2)

Input3 = "1256.256.256.256"
Output3 = "Neither"
print (validIPAddress(Input3) == Output3)

        