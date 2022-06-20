import json
from urllib.request import urlopen
url = "https://labsland.com/api/labs?&country=ES&lang=es"
response = urlopen(url)
datos = json.loads(response.read())
#if(key == 'educationLevels'):      NECESITO COGER SOLO EL DE LA UNI, LOS DEMAS A TOMAR POR CULO, CAMBIAR VARIABLES DE LOS FOR
          #  print(value[1])
print(type(datos))
for cosita in datos.values():
    for veremos in cosita:
        print(type(veremos))
        for key, value in veremos.items():
           if(key == 'educationLevels'):
               for prueba in value:
                   if(prueba == 'university'):
                       print("SOY UNIVERSITARIO, QUE LISTO SOY YO")
                   elif(prueba == 'ms'):
                       print("Estoy en la ESO")
                   elif(prueba == 'hs'):
                       print("Llegue a bachiller")
                   elif(prueba == 'elementary'):
                       print("Tengo miedo de ir al cole")

