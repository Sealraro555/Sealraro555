import random

caracteres = "+-_/*¡!&$#?¿=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("Introduce la longitud de la contraseña: "))
contraseña = ""

for i in range(longitud):
    contraseña += random.choice(caracteres)
print("La contraseña generada es:", contraseña)