from itertools import  combinations_with_replacement
import string

letras = list(string.ascii_lowercase + string.ascii_uppercase)

numbers = ["1","2","3","4","5","6","7","8","9","0" ] + letras
print(numbers)
combinations = []

for i in range(4):
    lista =list( combinations_with_replacement(numbers, i+1))
   
    for i in lista:
        combinations.append(i)


print(combinations)
print("Total combinaciones: ",len(combinations))
    

    

    
   

