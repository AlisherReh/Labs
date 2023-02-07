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
s.isdigit()
print()
