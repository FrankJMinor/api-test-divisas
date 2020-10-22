# -*- coding: utf-8 -*-

# standar library 
from datetime import datetime

# googletrans library
from googletrans import Translator

def traslate(text):
    traducir = Translator()
    message = traducir.translate(text, dest='ES').text
    print(message)