import qrcode
qr = qrcode.QRCode(version=1,
error_correction=qrcode.constants.ERROR_CORRECT_L,
box_size=20,
border=5)
giden_deyer = "Nümunə üçün hazırlanıbdır "
qr.add_data(giden_deyer)
qr.make(fit=True)

image=qr.make_image(fill_collor="black",back_color="White")
image.save("ilk_qr_code.png")
