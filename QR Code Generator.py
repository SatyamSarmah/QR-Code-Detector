import qrcode
import image
qrc=qrcode.QRCode(
    version=10,
    box_size=10,
    border=4
)

data=input()

qrc.add_data(data)
qrc.make(fit=True)
img=qrc.make_image(fill="black",back_color="white")
img.save("test.png")
