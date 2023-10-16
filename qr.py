import qrcode
import os
image=qrcode.make(input("enter any url:"))
image.save("qr.png")
os.system("qr.png")

