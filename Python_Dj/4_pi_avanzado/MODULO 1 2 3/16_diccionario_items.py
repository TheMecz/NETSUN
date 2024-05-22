d = {'a':1, 'b':2}
it = d.items()
print(it)             #dict_items([('a',1),('b',2)]) 
print(list(it))       #[('a',1),('b',2)]  
print(list(it)[0][0]) #a