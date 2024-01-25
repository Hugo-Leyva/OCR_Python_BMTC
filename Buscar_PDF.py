import fitz  # PyMuPDF
from PIL import Image
import pytesseract

# Ruta del ejecutable de Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def pdf_a_texto(pdf_path):
    # Abrir archivo PDF
    pdf_documento = fitz.open(pdf_path)

    # Concatenar el texto de todas las páginas en una sola cadena
    pdf_text = ''
    for num_paginas in range(pdf_documento.page_count):
        pagina = pdf_documento[num_paginas]
        #Aqui se hace el mapa de pixeles de la imagen y posterior se hace el OCR.
        pixmap = pagina.get_pixmap()
        imagen = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
        text_ocr = pytesseract.image_to_string(imagen)
        pdf_text += text_ocr

    # Cierra el documento PDF
    pdf_documento.close()

    return pdf_text

def buscar_en_pdf(pdf_text, palabra_a_buscar):
    
    # Convierte el texto y la palabra a minúsculas para hacer la búsqueda sin distinción de mayus o minus.
    pdf_text = pdf_text.lower()
    palabra_a_buscar = palabra_a_buscar.lower()

    # Verifica si la palabra está en el texto
    if palabra_a_buscar in pdf_text:
        # Encuentra la posición de la palabra en el texto
        inicio = pdf_text.find(palabra_a_buscar)
        fin = inicio + len(palabra_a_buscar)

        # Extrae la oración que contiene la palabra
        oracion = pdf_text[max(0, inicio - 30):min(len(pdf_text), fin + 30)]

        #contexto de la palabra
        oracion_resaltada = oracion.replace(palabra_a_buscar, f'*{palabra_a_buscar}*')

        # Imprime el resultado
        print(f"La palabra '{palabra_a_buscar}' se encuentra en el siguiente contexto:")
        print(oracion_resaltada)

        

    else:
        print("No se encuentra la palabra en el PDF.")
        

# Ruta al archivo PDF
pdf_path = 'CATALOGO CUENTAS.pdf'

# Llama a la función para convertir el PDF a texto utilizando Tesseract
pdf_text = pdf_a_texto(pdf_path)

while True:
    # Pide al usuario que ingrese la palabra a buscar
    palabra_a_buscar = input("Ingresa la palabra que deseas buscar en el PDF: ")

    # Llama a la función para buscar la palabra en el texto del PDF
    buscar_en_pdf(pdf_text, palabra_a_buscar)

    #¿Desea realizar otra busqueda?
    respuesta = int(input("\n¿Deseas realizar otra busqueda? Si: 1 NO: 2 "))
    if respuesta == 2:
        break
