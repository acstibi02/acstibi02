x1=int(input("Add meg A pont x koordinátáját: "))
y1=int(input("Add meg A pont y koordinátáját: "))
x2=int(input("Add meg B pont x koordinátáját: "))
y2=int(input("Add meg B pont y koordinátáját: "))

if x1>=x2:
    a=x1-x2
else:
    a=x2-x1
if y1>=y2:
    b=y1-y2
else:
    b=y2-y1
c=a**2+b**2

print(c**(0.5)," egység távolságra van A és B pont.")