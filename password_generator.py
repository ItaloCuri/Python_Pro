import random
#variable para la contrasenha

caracteres_contrasenha = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

#variable para lo largo de la contrasenha

longitud_contrasenha = int(input("pon la longitud de la contraseña segura que quieres generar:  "))

#contrasenha final

contrasenha = ""

#codigo al azar para sacar la contrasenha

for i in range (longitud_contrasenha):
    contrasenha += random.choice(caracteres_contrasenha)

#texto final:

print(f"tu contrasenha es:  {contrasenha}")
