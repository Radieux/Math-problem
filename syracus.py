print("""Pour connaître la suite de Syracus, merci de mettre le chiffre votre choix:""")

nombre = int(input())

def collatz(nombre):
    if nombre % 2 == 0:
        print (nombre, "est un chiffre pair")
    else:
        print (nombre, "est un chiffre impair")
    while nombre != 1:
        if nombre % 2 == 0:
            nombre //= 2
            print (nombre)
        elif nombre % 2 == 1:
            nombre *= 3
            nombre += 1 
            print (nombre)
            
collatz(nombre)     
