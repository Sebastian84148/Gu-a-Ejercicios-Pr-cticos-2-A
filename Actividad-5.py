edad = int(input("Ingrese su edad: "))
if edad < 10:
    print("Es un niño/a")
elif edad >= 10 and edad < 13:
    print("Es un pre-adolescente")
elif edad >= 13 and edad <= 17:
    print("Es un adolescente")
else: 
    print("Es mayor de edad")