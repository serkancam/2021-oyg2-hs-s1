import random
l1=[]
l2=[10,2,3]
l3=["ali",30,20.5]
l4=list()#l1 ve l4 boş liste oluşturur.
l1.append(30)
l1.append(40)
print(l1)
print(l3[0])
print(l3)

for _ in range(10):
    tut=random.randint(1,100)
    l4.append(tut)

print(l4)
enk=l4[0]
yer=0
for i in range(len(l4)):
    if l4[i]<enk:
        enk=l4[i]
        yer=i
print(f"en küçük sayı={enk} yeri={yer}")
A=[]#list()
while len(l4)!=0:
    enk=l4[0]
    yer=0
    for i in range(len(l4)):
        if l4[i]<enk:
            enk=l4[i]
            yer=i
    bulunan=l4.pop(yer)
    A.append(bulunan)
print(A)
    

