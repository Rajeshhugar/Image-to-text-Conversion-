import easyocr as ocr  #OCR
import os
#os.environ['KMP_DUPLICATE_LIB_OK']='True'
reader = ocr.Reader(['en'],model_storage_directory='.')

result = reader.readtext("outliers.jpeg")

for text in result:
    print(text[1])