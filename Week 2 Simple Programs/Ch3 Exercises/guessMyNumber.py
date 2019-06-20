def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    answer = 0.0    
    timesRun = 0.0
    while (exp - timesRun) > exp:
        answer += (base * base)
        timesRun += 1.0