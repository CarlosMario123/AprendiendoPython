"""
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
"""

#mi solucion
def high(x):
    #resta cada uno 96 por sus valores ascii
    #primero convertimos en arreglos en minuscula
    words = x.lower().split()
    #ahora iteramos
    winChar = ""#esta es la cadena ganadora
    valorMax = 0
    for word in words:
        valor = valueChar(word)
        if valor > valorMax:
            valorMax = valor
            winChar = word
    return winChar        

        
#usaremos la tecnica divide y venceras
def valueChar(word):
    valor = 0
    for w in word:
        valor += ord(w) - 96
    return valor


#solucion optimas
def highOptimize(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
