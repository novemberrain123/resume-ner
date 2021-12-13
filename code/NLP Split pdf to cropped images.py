#!/usr/bin/env python
# coding: utf-8

# In[4]:


from PIL import Image as PIimage
from PIL import ImageDraw
# import easyocr
import numpy as np
from IPython.display import display, Image
import sys
from pdf2image import convert_from_path
# import re 
# import spacy
# from spacy import displacy
import os

# reader = easyocr.Reader(['en'])
filecount = 1
directory = "C:/Users/razor/Desktop/NLP Assignment/Profile"
parent_storage_dir = "C:/Users/razor/Desktop/NLP Assignment/PDFimageDir"

for filename in os.listdir(directory):
    if filename.endswith(".pdf"): 
        PDF_path = os.path.join(directory, filename)       
        pages = convert_from_path(PDF_path, poppler_path = r"C:\Users\razor\Desktop\NLP\poppler-0.68.0\bin")
        
        store_file_directory = str(filename)
        path = os.path.join(parent_storage_dir, store_file_directory)
        os.mkdir(path)
        filecount += 1
        
        count = 1
        for number_of_pages in range(len(pages)):
            FirstCropped = pages[number_of_pages].crop((0,0,560,2200))
            SecondCropped = pages[number_of_pages].crop((560,0,1700,2200))
            # display(FirstCropped)
            FirstCropped = FirstCropped.save(path + "/" + str(count) + ".jpg")
            count += 1

            # display(SecondCropped)
            SecondCropped = SecondCropped.save(path + "/" + str(count) + ".jpg")
            count += 1    
    else:
        continue    


# In[35]:




