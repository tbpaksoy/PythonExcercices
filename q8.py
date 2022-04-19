#Hocanın çözümü
x = [1,2,3]
y = [.5,.7,.3]

z=list(map(lambda a,b:int(a*b),x,y))

print(z)

#Benim Çözümüm
print([int(i*j) for i,j in zip(x,y)])
