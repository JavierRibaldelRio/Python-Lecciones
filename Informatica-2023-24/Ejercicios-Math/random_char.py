from random import randint

word = input("Inserte una palabra: ")

print("Letra aleatoria:", word[randint(0,len(word)-1)])