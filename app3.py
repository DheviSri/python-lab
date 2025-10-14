import qrcode
data="https://moovit.vit.ac.in/"
qr=qrcode.make(data)
qr.save("moodle_qr.png")
print("QR code has been generated")