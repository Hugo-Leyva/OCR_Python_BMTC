from PIL import Image
import pytesseract

# Aquí especifico la ruta del ejecutable de tesseract.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Leer una imagen
img = Image.open('CV_IMAGEN.jpg')

# Realiza OCR en la imagen
texto = pytesseract.image_to_string(img)



# Pide al usuario que ingrese la palabra a buscar -------------------------------------
while True:
    palabra_a_buscar = input("Ingresa la palabra que deseas buscar: ")

    # Convierte el texto a minúsculas para hacer la búsqueda sin distinción entre mayúsculas y minúsculas
    texto = texto.lower()
    palabra_a_buscar = palabra_a_buscar.lower()

    # Verifica si la palabra está en el texto
    if palabra_a_buscar in texto:
        # Encuentra la posición de la palabra en el texto
        inicio = texto.find(palabra_a_buscar) #Inicio = posicion de la palabra
        fin = inicio + len(palabra_a_buscar) #fin es igual a la posicion de la palabra + la cant. de sus caracteres.

        # Variable que extrae la oracion donde aparece la palabra buscada.
        oracion = texto[max(0, inicio - 30):min(len(texto), fin + 30)]

        # Imprime la oración
        print(f"La palabra '{palabra_a_buscar}' se encuentra en la siguiente oración:\n")

        oracion_resaltada = oracion.replace(palabra_a_buscar, f'*{palabra_a_buscar}*')
        print(oracion_resaltada)


        #Preguntarle al usuario si desea realizar otra busqueda
        respuesta = int(input("\n¿Deseas realizar otra busqueda? Si: 1 NO: 2 "))
        if respuesta == 2:
            break
    else:
        print("No se encuentra la palabra en la imagen.")
        respuesta = int(input("\n¿Deseas realizar otra busqueda? Si: 1 NO: 2 "))
        if respuesta == 2:
            break
