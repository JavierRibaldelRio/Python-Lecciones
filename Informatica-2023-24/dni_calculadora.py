# Obtiene el DNI
dni = input("DNI (sin letra): ")

# Transforma el input a un Int
dni = int(dni)

# Equivalencias letras

equivalencias = "TRWAGMYFPDXBNJZSQVHLCKE"

print("Letra:", equivalencias[dni%23])