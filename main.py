import qrcode

qr = qrcode.QRCode(
  version=1,
  error_correction = qrcode.constants.ERROR_CORRECT_L,
  
  #Size of the "boxes" in the qrcode
  box_size=10,

  #Size of the qrcode
  border=4,
)

qr.add_data("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

img = qr.make_image()
img.save("qrcode.jpg")