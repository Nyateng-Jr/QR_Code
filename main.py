# install all libraries needed
# create a func that collect text and converts it to Qr code
# save QR code as image
# Run the function

import qrcode


def qrcode_generator(text):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#000000", back_color="#FFFFFF")
    img.save("qr_img.png")


url = input("Enter your url: ")
qrcode_generator(url)
