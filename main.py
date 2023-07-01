
import cv2
import pyqrcode
from pyzbar.pyzbar import decode
import time
import webbrowser

# # create a QR code
# link = 'https://www.jiosaavn.com/'
# url = pyqrcode.create(link)
# url.png('qrcodelink.png')

# print("QR Code link is created")

#read and scanning tht QR code from the webcam
cam = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
while True:
    _,img=cam.read()
    data,one, _=detector.detectAndDecode(img)
    if data:
        a=data
        break
    cv2.imshow('QRCode',img)
    if cv2.waitKey(1)==ord('q'):
        break
b=webbrowser.open(str(a))
cam.release(a)
cv2.destroyAllWindows()
#