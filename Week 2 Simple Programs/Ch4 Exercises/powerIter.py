def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    answer = 1.0    
    while exp != 0:
        answer *= base
        exp -= 1
    return answer