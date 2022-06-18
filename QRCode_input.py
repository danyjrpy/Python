#Instalar pacotes: pip install pyqrcode ; pip install pypng
import pyqrcode
import png 
from pyqrcode import QRCode

url = input(str("Cole a URL desejada: "))

QRStrink = url

url = pyqrcode.create(QRStrink)

url.png(r'qr.png', scale=8)
