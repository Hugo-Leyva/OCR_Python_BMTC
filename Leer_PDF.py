import fitz  # PyMuPDF
from PIL import Image
import pytesseract

# Se especifica la ruta al ejecutable de Tesseract.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def pdf_a_texto(pdf_path):
    # Abre el archivo PDF
    pdf_documento = fitz.open(pdf_path)

    # Itera a través de las páginas del PDF
    for page_number in range(pdf_documento.page_count):
        # Obtiene la página actual
        page = pdf_documento[page_number]

        # Obtiene el pixmap de la página como una imagen
        pixmap = page.get_pixmap()

        # Crea una imagen PIL desde el pixmap
        image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)

        # Realiza OCR en la imagen
        text_ocr = pytesseract.image_to_string(image)

        # Imprime el texto OCR
        print(f"\nTexto extraído de la página {page_number + 1}:\n")
        print(text_ocr)
        #separador
        print("-" * 50)

    # Cierra el documento PDF
    pdf_documento.close()

# Ruta al archivo PDF
pdf_path = 'CATALOGO CUENTAS.pdf'

# Llama a la función para convertir el PDF a texto utilizando Tesseract
pdf_a_texto(pdf_path)

