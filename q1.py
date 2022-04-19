#Benim yol
func = lambda x : x if x == 1 else x * func(x - 1)
print(func(int(input())))
# Hocanın yolu
from functools import reduce
n = 5
print(reduce(lambda a,b: a*b, [i for i in range(1,n+1)]))