def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    
    #base cases
    if aStr == '':
        return False
    if len(aStr) == 1:
        return aStr == char
    if aStr[len(aStr)//2] == char:
        return True
    
    #recursion
    elif char < aStr[len(aStr)//2]:
        return isIn(char, aStr[:(len(aStr)//2)])
    else:
        return isIn(char, aStr[(len(aStr)//2)+1:])
    
