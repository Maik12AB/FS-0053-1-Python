# range()
# Es una función de Python que devuelve un
# iterable con los valores pasados como
# argumentos

itera1 = range(10)

# Va de 0 a 9
print( itera1 )       # range(0, 10)
print( type(itera1) ) # <class 'range'>

print("Valores de itera1")
print("-----------------")
for i in itera1:
    print( i )

#-- - ------------------------------
itera2 = range(4, 10)

print()
print("Valores de itera2")
print("-----------------")
for i in itera2:
    print( i )

#-- - ------------------------------
itera3 = range(4, 10, 2)

print()
print("Valores de itera3")
print("-----------------")
for i in itera3:
    print( i )