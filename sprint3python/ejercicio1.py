import random

print ("El programa pensará un número entre 1 y un máximo que tú elijas. Intenta adivinarlo"
       "con la menor cantidad de intentos posibles")
print ("Elije la dificultad: Alta, Media o Baja")
dificultad = input ()
while dificultad not in ("Alta", "Media", "Baja"):
    dificultad = input ("Por favor, introduzca Alta, Media o Baja")
if dificultad == "Alta":
    numero = random.randint(1,500)
elif dificultad == "Media":
    numero = random.randint(1,100)
else:
    numero = random.randint(1,10)

print (f"Acierta el número entre 1 y { '500' if dificultad== 'Alta' else '200' if dificultad== 'Media' else '100' }")

intentosrealizados = 0

while True:
    estimación = int(input("Tu estimación: "))
    intentosrealizados += 1

    if estimación < numero:
        print("Tu estimación es muy baja.")
    elif estimación > numero:
        print("Tu estimación es muy alta.")
    else:
        print(f"Genial! Has adivinado el número en {intentosrealizados} intentos.")
        break