if __name__ == '__main__':
    s = input()
    alphanumeric = False
    alphabetical = False
    digits = False
    lowercase = False
    uppercase = False
    for c in s:
        
        if(c.isalnum()):
            alphanumeric = True
        if(c.isalpha()):
            alphabetical = True
        if(c.isdigit()):
            digits = True
        if(c.islower()):
            lowercase = True
        if(c.isupper()):
            uppercase = True
    print(alphanumeric)
    print(alphabetical)
    print(digits)
    print(lowercase)
    print(uppercase)
