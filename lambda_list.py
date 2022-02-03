import random
s = []
k = 20
for i in range(k):
    s.append(random.randint(0,101)) 
res = list(filter(lambda x: x < 20 or x > 25,s))
print('Начальный список: ',s,'\n','Без чисел от 20 до 25:',res,sep = '')
for i in range(k):
    s[i] = s[i]**2
print('Список квадратов:',s)
for i in range(len(res)):
    res[i] = res[i]**2
print('Список квадратов без чисел от 20 до 25:',res)



