s = 'HeLLo World'

class operation:
    def isupper(self):
        if('A'<i<'Z'):
            print('isupper')
        else:
            print('no')
    def islower(self):
        if('a'<i<'z'):
            print('islower')
        else:
            print('no')

k1 = 0
k2 = 0
for i in s:
    if('A'<i<'Z'):
        k1+=1
    if('a'<i<'z'):
        k2+=1
if(k1<k2):
    print(s.lower())
elif(k1>k2):
    print(s.upper())    

str = operation()
str.islower()
