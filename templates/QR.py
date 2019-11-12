import qrcode

ETH_Address = "0x89205A3A3b2A69De6Dbf7f01ED13B2108B2c43e7"
GasAVG = 160000
Data = ''

Message = 'ethereum:{}gas={}&data={}'.format(ETH_Address,GasAVG,Data)
qr = qrcode.QRCode(version=3, error_correction= qrcode.constants.ERROR_CORRECT_H, box_size=6 ,border=4)
qr.add_data(Message)
qr.make(fit=True)

img = qr.make_image()
img.save("QR.png")
print(Message)