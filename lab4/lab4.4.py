s = '45687'
print(s)
class operation:
    def isdigit(self):
        try:
            float(s)
            print('yes')
        except ValueError:
            print('no')

str = operation()
print()
print('Is digit?:')
str.isdigit()
print()
while True:
    try:
        a = int(input())
        b = int(input())
        sum = a+b
        print('sum: ', sum)
    except ValueError:
        print('Error')