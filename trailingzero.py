def trailingzero(n):
    res = 0
    for i in range(0,n):
        i = i*5
        res = res + n/i
    return res

def trailingZeroes(self, n: int) -> int:
        counter = 0
        while n>=5:
            counter += int(n/5)
            n = int(n/5)
        
        return counter