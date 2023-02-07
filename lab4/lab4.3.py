s = 'HeLLo World'

k1 = 0
k2 = 0
for i in s:
    if('A'<i<'Z'):
        k1+=1
    if('a'<i<'z'):
        k2+=1
if(k1<k2):
    if(s.islower()==True):
        print('Already lower')
    else:
        print(s.lower())
elif(k1>k2):
    if(s.isupper()==True):
        print('Already upper')
    else:
        print(s.upper())   


