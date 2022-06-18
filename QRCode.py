#Instalar pacotes: pip install pyqrcode ; pip install pypng
import pyqrcode
import png 
from pyqrcode import QRCode

#Link para o QRCode
QRStrink = "https://www.linkedin.com/in/danyjrpy/"

#Gerar o QR
url = pyqrcode.create(QRStrink)

#Salvar QR
url.png(r'qr.png', scale=8)