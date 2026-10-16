l=[i for i in range (100) if i%2==0]
print(l)

d5=(x: x**2 for x in (2,4,6))
print(d5)
d5.keys()
d5.values()
d5.items()

L=[0,1,2,1,4,5,1,1,0,5]
dico={0:L.count(0),1:L.count(1),2:L.count(2),4:L.count(4),5:L.count(5)}

dico2={x: L.count(x) for x in L}

dico1={}
for i in L:
    dico[i]=L.count(i)
print(dico1)

dico3{}
x=0
for i in L:
    if L[i]==i:
        x=x+1
        dico3[i]=x


l1=[i for i in range (50) if i%2==0]
l2=[x for x in l1]