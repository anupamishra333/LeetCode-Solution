#def fact(n):

#    if n ==0:
 #       return 1
  #  else:
   #     return n * fact(n-1)


# 
def fac(n):
    if n ==0:
        return 1
    temp = 1
    for i in range(0,n-1):
        temp = temp * i
        return temp

