""" 
The goal of this exercise is to convert a string to a new string where each character in the new string
is "(" if that 
character appears only once in the original string, or ")" if that character appears more than once in the o
riginal string. 
Ignore capitalization when determining if a character is a duplicate.


Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
"""

#mi solucion 
def duplicate_encode(word):
    # Paso 1: realizar el conteo
    conteo = {}
    mandar = "" # Palabra que mandaremos
    word_lower = word.lower()  # Convertir la palabra a minúsculas
    for t in word_lower:
        if t in conteo:
            conteo[t] += 1
        else:
            conteo[t] = 1
    # Paso 2: construir la cadena
    for t in word_lower:
        if conteo[t] == 1:
            mandar = mandar + "("
        else:
            mandar = mandar + ")"
    return mandar