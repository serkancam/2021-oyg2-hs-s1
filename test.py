import random

l=[]
for i in range(random.randint(2,10)):
    l.append(random.randint(100,1000))

l2=[random.randint(100,1000) for i in range(random.randint(2,10))]
print(len(l2))
print(len(l))

