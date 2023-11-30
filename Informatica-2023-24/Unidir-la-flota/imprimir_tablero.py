
equivalencias = [" ","O","X"]

def imprimir_tablero(tablero):

    letras = [" ","A","B","C","D","E","F","G","H","I","J"]

    filas = [0,1,2,3,4,5,6,7,8,9]

    def pri(ch, v=1,end=""):
        for i in range(0,v):
            print(ch,end=end)

    # Cabecera

    # Línia inicial
    pri("┌")
  


    for i in letras:

        pri("─",7)

        if i != "J":
            pri("┬")
        else:
            pri("┐")
    
    print()
    pri("│")

    for i in letras:

        pri(" ",3)
        pri(i,1,"")
        pri(" ",3)
        pri("│")

    print()
    pri("├")

    for i in letras:

        pri("─",7)

        if i != "J":
            pri("┼")
        else:
            pri("┤")
    
    
    n= 0
    for i in range(1,len(letras)):
        print()
        pri("│")

        pri(" ",3)
        pri(str(n))
        pri(" ",3)
        pri("│")

        n+=1

        for j in range(1,len(letras)):

        
            pri(" ",3)
            pri(equivalencias[tablero[i-1][j-1]])
            pri(" ",3)
            pri("│")
     


        if i != 10:

            print()
            pri("├")

            for j in letras:

                pri("─",7)

                if j != "J":
                    pri("┼")
                else:
                    pri("┤")
        
    print("")
    pri("└")

    for i in letras:

        pri("─",7)

        if i != "J":
            pri("┴")
        else:
            pri("┘")

    print()
