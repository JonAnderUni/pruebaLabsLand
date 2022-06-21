import json
from urllib.request import urlopen
import csv
url = "https://labsland.com/api/labs?&country=ES&lang=es"
respuesta = urlopen(url)
datosJSON = json.loads(respuesta.read())
#with open('labs.json') as archivo:
  #datosJSON = json.load(archivo)

data = ['Nombre Laboratorio', 'Descripcion Laboratorio', 'Institucion Laboratorio']
#      NECESITO COGER SOLO EL DE LA UNI, LOS DEMAS A TOMAR POR CULO, CAMBIAR VARIABLES DE LOS FOR
with open('laboratoriosUniversidad.csv','w') as file:
    write = csv.writer(file)
    write.writerow(data)
nombreLab = ''
descrLab = ''
institLab= ''


for dic_todo in datosJSON.values():
    for dic in dic_todo:

        paraImprimir = True
        for key, value in dic.items():

            if(key == 'institution'):
                institLab = value
            elif(key == 'description'):
                descrLab = value
            elif(key == 'name'):
                nombreLab = value
            elif(key == 'educationLevels'):
                for prueba in value:
                    if(prueba == 'hs' or prueba == 'ms'):
                        paraImprimir = False


        if (paraImprimir == True):
            lista = [nombreLab, descrLab, institLab]
            print(lista)
            with open('laboratoriosUniversidad.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow(lista)

