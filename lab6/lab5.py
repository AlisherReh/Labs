s = tuple(input().lower().split())
 
print( *tuple(i for i in s if 'ва' in i) )
